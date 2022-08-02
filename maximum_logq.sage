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
        instance = LWE.Parameters(n=n_dim, q=2**logq, Xs=secret_dist, Xe = error_dist)
        # alpha = 8/2**logq #(sigma*sqrt(2*pi)/2**logq).n()
        attack_costs = estimator(params = instance)
        # print(log(attack_costs["rop"], 2).n(),"curr logq", logq)
        return log(attack_costs["rop"], 2).n()
        

    def binary_search(logq_prev, logq_curr):
        lptr,rptr = logq_prev, logq_curr
        while lptr < rptr - 1:
            mid = floor((lptr + rptr)/2)
            print("mid = ", mid)
            security_mid = cost_estimating(mid)
            print("mid, security_mid", mid, security_mid)
            print("lptr,rptr", lptr,rptr)
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



#usvp-192bit
stddev = 3.19
secret_ternary = ND.Uniform(-1, 1)
error_gaussian = ND.DiscreteGaussian(stddev, mean=0, n=None)
logq_list_classical_usvp = []
logq_list_quantum_usvp = []
cost_model_classic = RC.BDGL16
cost_model_quantum = RC.LaaMosPol14
shape_model="gsa"
estimate_lwe_usvp_classic = partial(LWE.primal_usvp)#, red_shape_model=shape_model, red_cost_model = cost_model_classic)
estimate_lwe_usvp_quantum = partial(LWE.primal_usvp, red_shape_model=shape_model, red_cost_model = cost_model_quantum)
security_thres = 192
margin = 0
for n_s in [2**17, 2**16, 2**15, 2**14,2**13]:#, 2**13, 2**12]:
    logq_list_classical_usvp += [maximal_logq(estimate_lwe_usvp_classic, n_s, secret_ternary, error_gaussian, security_thres + margin, logq_initial = 800)]
    logq_list_quantum_usvp += [maximal_logq(estimate_lwe_usvp_quantum, n_s, secret_ternary, error_gaussian, security_thres + margin, logq_initial = 800)]
    print("n = ", n_s, " classical logq = ", logq_list_classical_usvp[-1], " quantum logq = ", logq_list_quantum_usvp[-1])
print("usvp classical: ", logq_list_classical_usvp)
print("usvp quantum: ", logq_list_quantum_usvp)