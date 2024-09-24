
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
# error_dist = ND.CenteredBinomial(21) central binormial distribution with 42 coins, std = 3.24
secret_mode = MODE_TERNARY # MODE_TERNARY or MODE_GAUSSIAN
cost_model_classical = RC.MATZOV
cost_model_quantum = RC.ChaLoy21#RC.LaaMosPol14
m = oo
n_list = [2**i for i in range(10, 18)]

# def initial_log_q(n, secret_dist, security_thres, power_setting):
#     # Use linear function to compute inital_log_q = slope*dimension + intercept
#     # Format: (slope, intercept)
#     coefficients = {
#         (128, MODE_TERNARY, "classical"): (0.02730, -7.09195),
#         (128, MODE_GAUSSIAN, "classical"): (0.02732, -13.93678),
#         (192, MODE_TERNARY, "classical"): (0.01885, -3.87931),
#         (192, MODE_GAUSSIAN, "classical"): (0.01885, -1.87931),
#         (256, MODE_TERNARY, "classical"): (0.01465, -3.08046),
#         (256, MODE_GAUSSIAN, "classical"): (0.01368, 15.95402),
#         (128, MODE_TERNARY, "quantum"): (0.02555, 2.08621),
#         (128, MODE_GAUSSIAN, "quantum"): (0.02557, -4.51724),
#         (192, MODE_TERNARY, "quantum"): (0.01757, -3.32184),
#         (192, MODE_GAUSSIAN, "quantum"): (0.01757, -1.32184),
#         (256, MODE_TERNARY, "quantum"): (0.01459, -19.25287),
#         (256, MODE_GAUSSIAN, "quantum"): (0.01362, -0.44253),
#     }
    
#     # Get the appropriate coefficients based on the inputs
#     key = (security_thres, secret_dist, power_setting)
#     if key in coefficients:
#         a, b = coefficients[key]
#         log_q = a * n + b
#         return round(log_q)
#     else:
#         return "Invalid input combination. Please check your inputs and try again."

def initial_log_q(n_dim, secret_dist, security_thres, power_setting):
    # Look-up table to retrieve the initial_log_q
    if n_dim < 1000 or n_dim > 2**17:
        return "Error: Only dimensions between 1000 and 2^17 (131072) are supported."
    
    # Define n_list
    n_list = [2**i for i in range(17, 9, -1)]
    
    # Lookup tables for classical settings
    logq_initial_classic_ternary = {
        128: {n_s: logq for n_s, logq in zip(n_list, [3523, 1747, 868, 431, 214, 107, 53, 26])},
        192: {n_s: logq for n_s, logq in zip(n_list, [2411, 1199, 597, 297, 148, 73, 36, 36])}, #dummy entry at the end
        256: {n_s: logq for n_s, logq in zip(n_list, [1866, 929, 463, 230, 114, 56, 27, 27])} #dummy entry at the end
    }

    logq_initial_classic_Gaussian = {
        128: {n_s: logq for n_s, logq in zip(n_list, [3525, 1749, 870, 433, 216, 109, 55, 29])},
        192: {n_s: logq for n_s, logq in zip(n_list, [2413, 1201, 599, 299, 150, 75, 38, 38])},#dummy entry at the end
        256: {n_s: logq for n_s, logq in zip(n_list, [1868, 931, 465, 232, 116, 59, 30, 30])}#dummy entry at the end
    }

    # Lookup tables for quantum settings
    logq_initial_quantum_ternary = {
        128: {n_s: logq for n_s, logq in zip(n_list, [3348, 1663, 825, 409, 203, 101, 50, 25])},
        192: {n_s: logq for n_s, logq in zip(n_list, [2301, 1145, 570, 283, 140, 69, 34, 34])},#dummy entry at the end
        256: {n_s: logq for n_s, logq in zip(n_list, [1784, 888, 442, 219, 108, 53, 26, 26])}#dummy entry at the end
    }

    logq_initial_quantum_Gaussian = {
        128: {n_s: logq for n_s, logq in zip(n_list, [3351, 1665, 827, 411, 205, 103, 52, 27])},
        192: {n_s: logq for n_s, logq in zip(n_list, [2304, 1147, 572, 285, 143, 72, 36, 36])},#dummy entry at the end
        256: {n_s: logq for n_s, logq in zip(n_list, [1786, 890, 445, 222, 111, 56, 28, 28])}#dummy entry at the end
    }
    
    # Select the appropriate lookup table based on power_setting and secret_dist
    if power_setting == "classical" and secret_dist == MODE_TERNARY:
        lookup_table = logq_initial_classic_ternary
    elif power_setting == "classical" and secret_dist == MODE_GAUSSIAN:
        lookup_table = logq_initial_classic_Gaussian
    elif power_setting == "quantum" and secret_dist == MODE_TERNARY:
        lookup_table = logq_initial_quantum_ternary
    elif power_setting == "quantum" and secret_dist == MODE_GAUSSIAN:
        lookup_table = logq_initial_quantum_Gaussian
    else:
        return "Invalid input combination. Please check your inputs and try again."
    
    # Get the appropriate log_q value
    try:
        log_q = lookup_table[security_thres][n_dim]
        # print(n_dim, log_q)
        return log_q
    except KeyError:
        return "Invalid input combination. Please check your inputs and try again."

ESTIMATORS = {
    "classical": {
        MODE_TERNARY: [
            partial(LWE.primal_usvp, red_cost_model=cost_model_classical),
                      partial(LWE.dual_hybrid, red_cost_model=cost_model_classical)
                      ,partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_classical)
                     ,partial(LWE.primal_bdd, red_cost_model=cost_model_classical)
                     ],
        MODE_GAUSSIAN: [
            partial(LWE.primal_usvp, red_cost_model=cost_model_classical),
                      partial(LWE.dual_hybrid, red_cost_model=cost_model_classical)
                      ,partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_classical)
                    ,partial(LWE.primal_bdd, red_cost_model=cost_model_classical)
                    ]
    },
    "quantum": {
        MODE_TERNARY: [
            partial(LWE.primal_usvp, red_cost_model=cost_model_quantum),
                      partial(LWE.dual_hybrid, red_cost_model=cost_model_quantum)
                      ,partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_quantum)
                      ,partial(LWE.primal_bdd, red_cost_model=cost_model_quantum)
                      ],
        MODE_GAUSSIAN: [
            partial(LWE.primal_usvp, red_cost_model=cost_model_quantum),
                      partial(LWE.dual_hybrid, red_cost_model=cost_model_quantum)
                      ,partial(LWE.primal_hybrid, mitm=False, babai=False, red_cost_model=cost_model_quantum)
            ,partial(LWE.primal_bdd, red_cost_model=cost_model_quantum)
                      ]
    }
}
def get_estimators_for_mode(secret_mode, power_setting, n_dim):
    # print(secret_mode, power_setting)
    estimators =  ESTIMATORS[power_setting][secret_mode]
    filtered_estimators = []
    for estimator in estimators:
        if n_dim > 2**14 and estimator.func == LWE.primal_hybrid:
            continue
        filtered_estimators.append(estimator)
    return filtered_estimators

def cost_estimating(estimator, logq, n_dim, secret_dist, error_dist, m = oo):
    try:
        instance = LWE.Parameters(n=n_dim, q=2**logq, Xs=secret_dist, Xe=error_dist, m=m)
        attack_costs = estimator(params=instance)
        return log(attack_costs["rop"], 2).n()
    
    except Exception as e:
        # Improved error handling with detailed debug information
        # print(f"Error during estimation: {e}")
        # print(f"DEBUG: logq = {logq}, n_dim = {n_dim}, secret_dist = {secret_dist}, error_dist = {error_dist}, m = {m}")
        # print(f"estimator: {estimator}")
        return None

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
    assert(cost_estimating(estimator, lptr+1, n_dim, secret_dist, error_dist)<security_target)
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
    logq_left, logq_right = logq_search_interval(estimator, n_dim, secret_dist, error_dist, security_target, logq_initial)
    maxlogq = binary_search(estimator, n_dim, secret_dist, error_dist, security_target, logq_left, logq_right)
    return maxlogq

def process_maxlogq(estimators, n_dim, secret_dist, error_dist, security_target, power_setting):
    logq_list = []
    for est in estimators:
        try:
            logq = maxlogq_finder(est, n_dim, secret_dist, error_dist, security_target, power_setting)
            # print(f"DEBUG:{n_dim}, {est}")
            logq_list.append(logq)
        except Exception as e:
            # print(f"Error encountered with estimator {est.func.__name__} at n_dim={n_dim}: {e}")
            continue
    if not logq_list:
        # Handle the case where all estimators fail
        raise RuntimeError(f"All estimators failed for n_dim={n_dim}. Unable to compute logq.")
    
    # print(f"DEBUG: maxlogq list = {logq_list}")
    return min(logq_list)

secret = {MODE_TERNARY: "ternary", MODE_GAUSSIAN: "Gaussian"}

if __name__ == "__main__":
    security_thres = int(sys.argv[1])
    security_margin = int(sys.argv[2])
    include_quantum = sys.argv[3].lower() == "true" if len(sys.argv) > 3 else False

security_target = security_thres + security_margin
print(f"security threshold = {security_thres}, margin = {security_margin}, target = {security_target}")

# Define headers conditionally based on whether quantum columns are included
if include_quantum:
    headers = ["n", "Classical Ternary", "Classical Gaussian", "Quantum Ternary", "Quantum Gaussian"]
else:
    headers = ["n", "Classical Ternary", "Classical Gaussian"]

# Format headers dynamically based on the selected columns
header_format = "| {:<{}s} | {:<{}s} | {:<{}s} ".format(
    headers[0], 8,
    headers[1], 17,
    headers[2], 18
)
if include_quantum:
    header_format += "| {:<{}s} | {:<{}s} |".format(headers[3], 15, headers[4], 16)
else:
    header_format += "|"

separator = "+" + "-" * (10) + "+" + "-" * (19) + "+" + "-" * (20) + "+"
if include_quantum:
    separator += "+" + "-" * (17) + "+" + "-" * (18) + "+"
    
border = "-" * (90 if include_quantum else 53)

print(border)
print(header_format)
print(separator)

for n_dim in n_list:
    if n_dim < 2048 and security_target > 130:
        continue

    logq_classical_ternary = []
    logq_classical_gaussian = []
    logq_quantum_ternary = []
    logq_quantum_gaussian = []

    for power in ["classical", "quantum"] if include_quantum else ["classical"]:
        for secret_mode in [MODE_TERNARY, MODE_GAUSSIAN]:
            estimators = get_estimators_for_mode(secret_mode, power, n_dim)
            logq = process_maxlogq(estimators, n_dim, secret_mode, error_dist, security_target, power)
            if power == "classical" and secret_mode == MODE_TERNARY:
                logq_classical_ternary.append(logq)
            elif power == "classical" and secret_mode == MODE_GAUSSIAN:
                logq_classical_gaussian.append(logq)
            elif power == "quantum" and secret_mode == MODE_TERNARY:
                logq_quantum_ternary.append(logq)
            elif power == "quantum" and secret_mode == MODE_GAUSSIAN:
                logq_quantum_gaussian.append(logq)

    row_format = "| {:<{}} | {:<{}} | {:<{}} ".format(
        n_dim, 8,
        logq_classical_ternary[0], 17,
        logq_classical_gaussian[0], 18
    )
    
    if include_quantum:
        row_format += "| {:<{}} | {:<{}} |".format(
            logq_quantum_ternary[0], 15,
            logq_quantum_gaussian[0], 16
        )
    else:
        row_format += "|"
        
    print(row_format)
    print(separator)





