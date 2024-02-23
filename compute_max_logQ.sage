
mport sys
sys.path.insert(1, 'lattice-estimator')

from estimator import *
from functools import partial
import time


MODE_TERNARY = "ternary"
MODE_GAUSSIAN = "gaussian"
#sparse
MODE_SPARSE = "sparse"
hamming_weights = [128, 192, 256]

stddev = 3.19
error_dist = ND.DiscreteGaussian(stddev, mean=0, n=None)
secret_mode = MODE_TERNARY # MODE_TERNARY or MODE_SPARSE or MODE_GAUSSIAN
cost_model_classic = RC.BDGL16
cost_model_quantum = RC.LaaMosPol14
m = oo
security_margin = 0
security_margin_sparse = 2
n_list = [2**i for i in range(17, 10, -1)]
logq_initial_classic = {
    128: {n_s: logq for n_s, logq in zip(n_list, [3575, 1775, 881, 437, 218, 110, 55])},
    192: {n_s: logq for n_s, logq in zip(n_list, [2462, 1225, 610, 304, 151, 80, 40])},
    256: {n_s: logq for n_s, logq in zip(n_list, [1912, 953, 475, 237, 118, 60, 30])}
}

logq_initial_quantum = {
    128: {n_s: logq for n_s, logq in zip(n_list, [3337, 1662, 825, 409, 204, 110, 55])},
    192: {n_s: logq for n_s, logq in zip(n_list, [2300, 1143, 569, 284, 141, 80, 40])},
    256: {n_s: logq for n_s, logq in zip(n_list, [1781, 887, 443, 220, 109, 60, 30])}
}
n_list = sorted(n_list)  #If we want to find parameters from smallest dimension to largest.
print(n_list)
# ESTIMATORS = {
#     "classic": {
#         "ternary": [partial(LWE.primal_usvp, red_cost_model=cost_model_classic),
#                       partial(LWE.dual_hybrid, red_cost_model=cost_model_classic)],
#         "gaussian": [partial(LWE.primal_usvp, red_cost_model=cost_model_classic),
#                       partial(LWE.dual_hybrid, red_cost_model=cost_model_classic)],
#         "sparse": [partial(LWE.dual_hybrid, red_cost_model=cost_model_classic, mitm_optimization=True)]
#     },
#     "quantum": {
#         "ternary": [partial(LWE.primal_usvp, red_cost_model=cost_model_quantum),
#                       partial(LWE.dual_hybrid, red_cost_model=cost_model_quantum)],
#         "gaussian": [partial(LWE.primal_usvp, red_cost_model=cost_model_quantum),
#                       partial(LWE.dual_hybrid, red_cost_model=cost_model_quantum)],
#         "sparse": [partial(LWE.dual_hybrid, red_cost_model=cost_model_quantum, mitm_optimization=True)]
#     }
# }

ESTIMATORS = {
    "classic": {
        "ternary": [partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_classic)],
        "gaussian": [partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_classic)],
        "sparse": [partial(LWE.dual_hybrid, red_cost_model=cost_model_classic, mitm_optimization=True)]
    },
    "quantum": {
        "ternary": [partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_quantum)],
        "gaussian": [partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_quantum)],
        "sparse": [partial(LWE.dual_hybrid, red_cost_model=cost_model_quantum, mitm_optimization=True)]
    }
}

def set_secret_distribution(secret_mode, n_s=None, hamming_weight=None):
    distributions = {
        MODE_TERNARY: ND.Uniform(-1, 1),
        MODE_GAUSSIAN: ND.DiscreteGaussian(stddev, mean=0, n=None)
    }
    if secret_mode == MODE_SPARSE:
        if hamming_weight is None:
            raise ValueError("Hamming weight is required for MODE_SPARSE.")
        distributions[MODE_SPARSE] = ND.SparseTernary(n_s, hamming_weight // 2, hamming_weight - hamming_weight // 2)

    if secret_mode not in distributions:
        raise ValueError(f"The following secret distribution mode is not yet included in the tables: {secret_mode}")
    
    return distributions[secret_mode]

def cost_estimating(estimator, logq, n_dim, secret_dist, error_dist):
    instance = LWE.Parameters(n=n_dim, q=2**logq, Xs=secret_dist, Xe=error_dist, m=m)
    start_time = time.time()
    print(n_dim, logq)
    attack_costs = estimator(params=instance)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("security = ", log(attack_costs["rop"], 2).n())
    print(f"Elapsed time: {elapsed_time} seconds")
    return log(attack_costs["rop"], 2).n()

def binary_search(estimator, n_dim, secret_dist, error_dist, security_target, logq_prev, logq_curr):
    lptr, rptr = logq_prev, logq_curr
    while lptr < rptr - 1:
        mid = floor((lptr + rptr) / 2)
        security_mid = cost_estimating(estimator, mid, n_dim, secret_dist, error_dist)
        
        if security_mid < security_target:
            rptr = mid
        elif security_mid >= security_target + 0.01:
            lptr = mid
        else:
            return mid
    return lptr

def logq_find_interval(estimator, n_dim, secret_dist, error_dist, security_target, logq_initial_per_level_per_dim, logq_interval=20):
    logq_curr = logq_initial_per_level_per_dim
    while True:
        security_curr = cost_estimating(estimator, logq_curr, n_dim, secret_dist, error_dist)
        if security_curr < security_target:
            logq_prev = logq_curr - logq_interval
            security_prev = cost_estimating(estimator, logq_prev, n_dim, secret_dist, error_dist)
            while security_prev < security_target:
                logq_prev -= logq_interval
                security_prev = cost_estimating(estimator, logq_prev, n_dim, secret_dist, error_dist)
            return binary_search(estimator, n_dim, secret_dist, error_dist, security_target, logq_prev, logq_curr)
        else:
            logq_curr += logq_interval

def logq_find_max(estimator, n_list, secret_mode, error_dist, security_target, logq_initial_per_level, hamming_weight=None):
    """Find the specific maximal logq for a given estimator and parameters."""
    print("Using estimator:", estimator)
    logq_max_list = []
    for n_s in n_list:
        # Determine secret distribution based on mode
        secret_dist = set_secret_distribution(secret_mode, n_s, hamming_weight)
        logq_max = logq_find_interval(estimator, n_s, secret_dist, error_dist, security_target, logq_initial_per_level[n_s])
        logq_max_list.append(logq_max)
    
    print("logq_max_list = ", logq_max_list)
    return logq_max_list

def process_logq(security_target, estimator_classic, estimator_quantum, n_list, secret_mode, error_dist, hamming_weight, logq_initial_classic_per_level, logq_initial_quantum_per_level):
    logq_classical = logq_find_max(estimator_classic, n_list, secret_mode, error_dist, security_target, logq_initial_classic_per_level, hamming_weight)
    print("classical max_logq", logq_classical)
    logq_quantum = logq_find_max(estimator_quantum, n_list, secret_mode, error_dist, security_target, logq_initial_quantum_per_level, hamming_weight)
    print("quantum max_logq", logq_quantum)
    return logq_classical, logq_quantum

def get_estimators_for_mode(secret_mode):
    print(secret_mode)
    return ESTIMATORS["classic"][secret_mode], ESTIMATORS["quantum"][secret_mode]

for security_thres in [128, 192, 256]:
    security_target = security_thres + (security_margin_sparse if secret_mode == MODE_SPARSE else security_margin)
    print(f"security threshold = {security_thres}, margin = {security_target - security_thres}")
    
    all_logq_classical, all_logq_quantum = [], []
    hamming_weights = [128, 192, 256] if secret_mode == MODE_SPARSE else [None]

    for hamming_weight in hamming_weights:
        if hamming_weight:  # This check ensures we only print for sparse mode
            print(f"hamming_weight = {hamming_weight}")
        
        estimators_classic, estimators_quantum = get_estimators_for_mode(secret_mode)
        for estimator_classic, estimator_quantum in zip(estimators_classic, estimators_quantum):
            logq_classical, logq_quantum = process_logq(security_target, estimator_classic, estimator_quantum, n_list, secret_mode, error_dist, hamming_weight, logq_initial_classic[security_thres], logq_initial_quantum[security_thres])
            
            all_logq_classical.append(logq_classical)
            all_logq_quantum.append(logq_quantum)

    minimal_logq_classical = [min(logq) for logq in zip(*all_logq_classical)]
    minimal_logq_quantum = [min(logq) for logq in zip(*all_logq_quantum)]

    print(f"classic {secret_mode}", minimal_logq_classical)
    print(f"quantum {secret_mode}", minimal_logq_quantum)
    print("-------------------------------------")


