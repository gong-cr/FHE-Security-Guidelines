
import sys
sys.path.insert(1, 'lattice-estimator')

from estimator import *
from functools import partial
from sage.all import oo, log
import time

MODE_TERNARY = ND.Uniform(-1, 1)
MODE_GAUSSIAN = ND.DiscreteGaussian(stddev=3.19, mean=0, n=None)
#NOTE: sparse-LWE is currently not recommended in the guideline 2/16/2024

error_dist = ND.DiscreteGaussian(stddev=3.19, mean=0, n=None)
secret_mode = MODE_TERNARY # MODE_TERNARY or MODE_GAUSSIAN
cost_model_classical = RC.MATZOV
cost_model_quantum = RC.LaaMosPol14
m = oo
security_margin = 0
n_list = [2**i for i in range(10, 18)]

def initial_log_q(n, secret_dist, security_thres, power_setting):
    # Define the linear coefficients for each scenario
    # Format: (slope, intercept)
    coefficients = {
        (128, MODE_TERNARY, "classical"): (0.02730, -7.09195),
        (128, MODE_GAUSSIAN, "classical"): (0.02732, -13.93678),
        (192, MODE_TERNARY, "classical"): (0.01885, -3.87931),
        (192, MODE_GAUSSIAN, "classical"): (0.01885, -1.87931),
        (256, MODE_TERNARY, "classical"): (0.01465, -3.08046),
        (256, MODE_GAUSSIAN, "classical"): (0.01368, 15.95402),
        (128, MODE_TERNARY, "quantum"): (0.02555, 2.08621),
        (128, MODE_GAUSSIAN, "quantum"): (0.02557, -4.51724),
        (192, MODE_TERNARY, "quantum"): (0.01757, -3.32184),
        (192, MODE_GAUSSIAN, "quantum"): (0.01757, -1.32184),
        (256, MODE_TERNARY, "quantum"): (0.01459, -19.25287),
        (256, MODE_GAUSSIAN, "quantum"): (0.01362, -0.44253),
    }
    
    # Get the appropriate coefficients based on the inputs
    key = (security_thres, secret_dist, power_setting)
    if key in coefficients:
        a, b = coefficients[key]
        log_q = a * n + b
        return round(log_q)
    else:
        return "Invalid input combination. Please check your inputs and try again."

ESTIMATORS = {
    "classical": {
        MODE_TERNARY: [partial(LWE.primal_usvp, red_cost_model=cost_model_classical),
                      partial(LWE.dual_hybrid, red_cost_model=cost_model_classical)
                    #   ,partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_classical)
                     ],
        MODE_GAUSSIAN: [partial(LWE.primal_usvp, red_cost_model=cost_model_classical),
                      partial(LWE.dual_hybrid, red_cost_model=cost_model_classical)
                    #   ,partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_classical)
                    ]
    },
    "quantum": {
        MODE_TERNARY: [partial(LWE.primal_usvp, red_cost_model=cost_model_quantum),
                      partial(LWE.dual_hybrid, red_cost_model=cost_model_quantum)
                    #   ,partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_quantum)
                      ],
        MODE_GAUSSIAN: [partial(LWE.primal_usvp, red_cost_model=cost_model_quantum),
                      partial(LWE.dual_hybrid, red_cost_model=cost_model_quantum)
                    #   ,partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_quantum)
                      ]
    }
}
def get_estimators_for_mode(secret_mode, power_setting):
    # print(secret_mode, power_setting)
    return ESTIMATORS[power_setting][secret_mode]

def cost_estimating(estimator, logq, n_dim, secret_dist, error_dist):
    instance = LWE.Parameters(n=n_dim, q=2**logq, Xs=secret_dist, Xe=error_dist, m=m)
    # start_time = time.time()
    attack_costs = estimator(params=instance)
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print("security = ", log(attack_costs["rop"], 2).n())
    # print(f"Elapsed time: {elapsed_time} seconds")
    return log(attack_costs["rop"], 2).n()

def binary_search(estimator, n_dim, secret_dist, error_dist, security_target, logq_left, logq_right):
    """
    Output logQ such that 
    security_estimation(2**logQ, ...) >= security_target 
     AND
    security_estimation(2**（logQ + 1）, ...) < security_target
    """
    lptr, rptr = logq_left, logq_right 
    while lptr < rptr:
        mid = (lptr + rptr + 1) // 2
        security_mid = cost_estimating(estimator, mid, n_dim, secret_dist, error_dist)
        if security_mid >= security_target:
            lptr = mid
        else:
            rptr = mid - 1
    assert(cost_estimating(estimator, lptr, n_dim, secret_dist, error_dist)>=security_target)
    return lptr  #lptr == rptr

def logq_search_interval(estimator, n_dim, secret_mode, error_dist, security_target, logq_initial, logq_interval=20):
    """
    Output logq_left, logq_right as left bound and right bound for maxlogQ binary search
    security_estimation(2**logQ_left, ...) >= security_target
    security_estimation(2**logQ_right, ...) < security_target
    """
    if n_dim < 1200:
        logq_interval = 5
    logq_left = logq_initial
    logq_right = None

    while True:#find the left bound where security just exceeds the target.
        security_left = cost_estimating(estimator, logq_left, n_dim, secret_mode, error_dist)
        if security_left >= security_target:
            break # Found the left bound where security meets/exceeds the target
        else: #logq_right is found
            logq_right = logq_left
            logq_left -= logq_interval
    
    if logq_right is None:#only when logq_left is found during the first iteration of the first while loop
        logq_right = logq_initial + logq_interval
        while True:
            security_right = cost_estimating(estimator, logq_right, n_dim, secret_mode, error_dist)
            if security_right < security_target:
                break
            else:
                logq_right += logq_interval
    # print(f"DEBUG: search range: {logq_left, logq_right}")
    return logq_left, logq_right

def maxlogq_finder(estimator, n_dim, secret_dist, error_dist, security_target, power_setting):
    """Find the specific maximal logq for a given estimator and parameters."""
    # print("Using estimator:", estimator)
    logq_initial = initial_log_q(n_dim, secret_dist, security_thres, power_setting)
    # Determine secret distribution based on mode
    logq_left, logq_right = logq_search_interval(estimator, n_dim, secret_dist, error_dist, security_target, logq_initial)
    maxlogq = binary_search(estimator, n_dim, secret_dist, error_dist, security_target, logq_left, logq_right)
    return maxlogq

def process_maxlogq(estimators, n_dim, secret_dist, error_dist, security_target, power_setting):
    logq_list = []
    for est in estimators:
        # print(f"DEBUG: {est}")
        logq = maxlogq_finder(est, n_dim, secret_dist, error_dist, security_target, power_setting)
        logq_list.append(logq)
    # print(f"security target ={security_target}")
    # print(f"DEBUG: maxlogq list = {logq_list}")
    return min(logq_list)

secret = {MODE_TERNARY: "ternary", MODE_GAUSSIAN: "Gaussian"}

if __name__ == "__main__":
    security_thres = int(sys.argv[1])

security_target = security_thres + security_margin
print(f"security threshold = {security_thres}, margin = {security_margin}, target = {security_target}")
for n_dim in n_list:
    if n_dim < 2048 and security_target > 130:
            continue
    print(f"dim = {n_dim}")
    for power in ["classical", "quantum"]:
        for secret_mode in [MODE_TERNARY, MODE_GAUSSIAN]:
            estimators = get_estimators_for_mode(secret_mode, power)
            logq = process_maxlogq(estimators, n_dim, secret_mode, error_dist, security_target, power)
            print(f"{power} {secret[secret_mode]}, max logq = {logq}")
    print("-------------------------------------")


