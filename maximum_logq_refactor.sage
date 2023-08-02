import sys
sys.path.insert(1, 'lattice-estimator')
from estimator import *
from functools import partial

def maximal_logq(estimator, n_dim, secret_dist, error_dist, security_thres, logq_initial = 5):
    '''
    estimator uses lattice estimator not lweestimator
    compute the maximal logq such that the bit security >= security_thres
    '''
    def cost_estimating(logq):
        #return log of cost
        # print("n_dim, 2**logq ", n_dim, logq)
        instance = LWE.Parameters(n=n_dim, q=2**logq, Xs=secret_dist, Xe = error_dist, m = oo)
        # alpha = 8/2**logq #(sigma*sqrt(2*pi)/2**logq).n()
        attack_costs = estimator(params = instance)
        # print(log(attack_costs["rop"], 2).n(),"curr logq", logq)
        return log(attack_costs["rop"], 2).n()
        

    def binary_search(logq_prev, logq_curr):
        lptr,rptr = logq_prev, logq_curr
        while lptr < rptr - 1:
            mid = floor((lptr + rptr)/2)
            # print("mid = ", mid)
            security_mid = cost_estimating(mid)
            # print("mid, security_mid", mid, security_mid)
            # print("lptr,rptr", lptr,rptr)
            if security_mid < security_thres:
                rptr = mid
            elif security_mid >= security_thres + 1:
                lptr = mid
            else:
                # print("testing: mid security: ", security_mid)
                return mid
        # print("testing: lptr security: ", cost_estimating(lptr))
        return lptr

    logq_curr = logq_initial
    #Choose left pointer and right pointer for binary_search
    while True:
        # print("log q:", logq_curr)
        security_curr = cost_estimating(logq_curr)
        # print("security_curr = ", security_curr)
        if security_curr < security_thres:
            logq_prev = logq_curr/2
            security_prev = cost_estimating(logq_prev)
            while security_prev < security_thres:
                logq_prev = logq_prev/2
                security_prev = cost_estimating(logq_prev)
            #     print("testing: (logq_prev, security_prev) ", logq_prev, security_prev)
            # print("testing: finish loop")
            return binary_search(logq_prev, logq_curr)
        else:
            # print("else")
            logq_curr *=2

def maximal_logq_interval(estimator, n_dim, secret_dist, error_dist, security_thres, logq_initial, logq_interval = 20):
    '''
    estimator uses lattice estimator not lweestimator
    compute the maximal logq such that the bit security >= security_thres
    '''
    # print("logq_initial", logq_initial)
    def cost_estimating(logq):
        #return log of cost
        # print("n_dim, 2**logq ", n_dim, logq)
        instance = LWE.Parameters(n=n_dim, q=2**logq, Xs=secret_dist, Xe = error_dist, m = oo)
        # alpha = 8/2**logq #(sigma*sqrt(2*pi)/2**logq).n()
        # print(n_dim, logq)
        attack_costs = estimator(params = instance)
        # print(log(attack_costs["rop"], 2).n(),"curr logq", logq)
        return log(attack_costs["rop"], 2).n()
        

    def binary_search(logq_prev, logq_curr):
        lptr,rptr = logq_prev, logq_curr
        while lptr < rptr - 1:
            mid = floor((lptr + rptr)/2)
            # print("mid = ", mid)
            security_mid = cost_estimating(mid)
            # print("mid, security_mid", mid, security_mid)
            # print("lptr,rptr", lptr,rptr)
            if security_mid < security_thres:
                rptr = mid
            elif security_mid >= security_thres + 1:
                lptr = mid
            else:
                # print("testing: mid security: ", security_mid)
                return mid
        # print("testing: lptr security: ", cost_estimating(lptr))
        return lptr

    logq_curr = logq_initial
    #Choose left pointer and right pointer for binary_search
    while True:
        # print("log q:", logq_curr)
        security_curr = cost_estimating(logq_curr)
        # print("security_curr = ", security_curr)
        if security_curr < security_thres:
            logq_prev = logq_curr - logq_interval
            security_prev = cost_estimating(logq_prev)
            while security_prev < security_thres:
                logq_prev = logq_prev - logq_interval
                security_prev = cost_estimating(logq_prev)
            #     print("testing: (logq_prev, security_prev) ", logq_prev, security_prev)
            # print("testing: finish loop")
            return binary_search(logq_prev, logq_curr)
        else:
            # print("else")
            logq_curr += logq_interval


stddev = 3.19
secret_ternary = ND.Uniform(-1, 1) #ND.UniformMod(3)#ND.UniformMod(3)#ND.Uniform(-1, 1)
error_gaussian = ND.DiscreteGaussian(stddev, mean=0, n=None)
cost_model_classic = RC.BDGL16
cost_model_quantum = RC.LaaMosPol14
m = oo

logq_list_classical_usvp = []
logq_list_quantum_usvp = []
logq_list_classical_dual = []
logq_list_quantum_dual = []
logq_list_classical_dualH = []
logq_list_quantum_dualH = []

estimate_lwe_usvp_classic = partial(LWE.primal_usvp, red_cost_model = cost_model_classic)
estimate_lwe_usvp_quantum = partial(LWE.primal_usvp, red_cost_model = cost_model_quantum)

estimate_lwe_dual_classic = partial(LWE.dual, red_cost_model = cost_model_classic)
estimate_lwe_dual_quantum = partial(LWE.dual, red_cost_model = cost_model_quantum)

estimate_lwe_dualH_classic = partial(LWE.dual_hybrid, red_cost_model = cost_model_classic)
estimate_lwe_dualH_quantum = partial(LWE.dual_hybrid, red_cost_model = cost_model_quantum)

security_thres = 256
margin = 0
n_list = [2**17, 2**16, 2**15, 2**14, 2**13]

for n_s in n_list:#, 2**13, 2**12]:
    
    logq_list_classical_usvp += [maximal_logq(estimate_lwe_usvp_classic, n_s, secret_ternary, error_gaussian, security_thres + margin, logq_initial = 800)]
    logq_list_quantum_usvp += [maximal_logq(estimate_lwe_usvp_quantum, n_s, secret_ternary, error_gaussian, security_thres + margin, logq_initial = 800)]
print("usvp classical: ", logq_list_classical_usvp)
print("usvp quantum: ", logq_list_quantum_usvp)

def create_dict(keys, values):
    if len(keys) != len(values):
        raise ValueError("Number of keys and values must be the same.")
    
    return dict(zip(keys, values))

initial_classic_dict = create_dict(n_list, logq_list_classical_usvp)
initial_quantum_dict = create_dict(n_list, logq_list_quantum_usvp)

for n_s in n_list:
    logq_list_classical_dual += [maximal_logq_interval(estimate_lwe_dual_classic, n_s, secret_ternary, error_gaussian, security_thres + margin, logq_initial = initial_classic_dict[n_s])]
    logq_list_quantum_dual += [maximal_logq_interval(estimate_lwe_dual_quantum, n_s, secret_ternary, error_gaussian, security_thres + margin, logq_initial = initial_quantum_dict[n_s])]
    # # print("DUAL finish")
    logq_list_classical_dualH += [maximal_logq_interval(estimate_lwe_dualH_classic, n_s, secret_ternary, error_gaussian, security_thres + margin, logq_initial = initial_classic_dict[n_s])]
    logq_list_quantum_dualH += [maximal_logq_interval(estimate_lwe_dualH_quantum, n_s, secret_ternary, error_gaussian, security_thres + margin, logq_initial = initial_quantum_dict[n_s])]

print("dual classical: ", logq_list_classical_dual)
print("dual quantum: ", logq_list_quantum_dual)

print("dualH classical: ", logq_list_classical_dualH)
print("dualH quantum: ", logq_list_quantum_dualH)

# 128
# usvp classical:  [3575, 1775, 881, 437, 218]
# usvp quantum:  [3337, 1662, 825, 409, 204]
# dual classical:  [3576, 1777, 882, 439, 218]
# dual quantum:  [3347, 1664, 826, 410, 205]
# dualH classical:  [3576, 1777, 881, 438, 218]
# dualH quantum:  [3347, 1664, 826, 410, 204]


#192
# usvp classical:  [2462, 1225, 610, 304, 151]
# usvp quantum:  [2300, 1143, 569, 284, 141]
# dualH classical:  [2467, 1227, 611, 304, 151]
# dualH quantum:  [2302, 1145, 570, 284, 141]

#256
usvp classical:  [1912, 953, 475, 237, 118]
usvp quantum:  [1781, 887, 443, 220, 109]
dual classical:  [1917, 955, 476, 237, 118]
dual quantum:  [1783, 889, 443, 221, 110]
dualH classical:  [1917, 955, 475, 237, 117]
dualH quantum:  [1783, 889, 442, 220, 109]
# n_s = 2**14

# logq_list_classical_dual += [maximal_logq_interval(estimate_lwe_dual_classic, n_s, secret_ternary, error_gaussian, security_thres + margin, 304)]
# logq_list_quantum_dual += [maximal_logq_interval(estimate_lwe_dual_quantum, n_s, secret_ternary, error_gaussian, security_thres + margin, 284)]
# print("dual classical: ", logq_list_classical_dual)
# print("dual quantum: ", logq_list_quantum_dual)