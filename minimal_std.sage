from estimator import *
from functools import partial


def minimal_stddev(estimator, n_dim, logq, secret_dist, security_thres, log_stddev_initial = 1):
    '''
    estimator uses lattice estimator not lweestimator
    compute the maximal logq such that the bit security >= security_thres
    '''
    
    def cost_estimating(log_stddev):
        #return log of cost
        print("n_dim, 2**logq, log_stddev ", n_dim, logq, log_stddev)
        error_dist = ND.DiscreteGaussian(2**log_stddev, mean=0, n=None)
        instance = LWE.Parameters(n=n_dim, q=2**logq, Xs=secret_dist, Xe = error_dist)
        # alpha = 8/2**logq #(sigma*sqrt(2*pi)/2**logq).n()
        attack_costs = estimator(params = instance)
        print("security", log(attack_costs["rop"], 2).n(),"curr stddev", log_stddev)
        return log(attack_costs["rop"], 2).n()
        

    def binary_search(stddev_prev, stddev_curr):
        lptr,rptr = stddev_prev, stddev_curr
        while lptr < rptr - 1:
            mid = floor((lptr + rptr)/2)
            print("mid = ", mid)
            security_mid = cost_estimating(mid)
            print("mid, security_mid", mid, security_mid)
            print("lptr,rptr", lptr,rptr)
            if security_mid < security_thres:
                lptr = mid
            elif security_mid >= security_thres + 1:
                rptr = mid
            else:
                print("testing: mid security: ", security_mid)
                return mid
        print("testing: lptr security: ", cost_estimating(lptr))
        return rptr

    stddev_curr = log_stddev_initial
    #Choose left pointer and right pointer for binary_search
    while True:
        # print("std dev:", stddev_curr)
        security_curr = cost_estimating(stddev_curr)
        # print("security_curr = ", security_curr)
        if security_curr < security_thres:
            print("security_curr < security_thres")
            stddev_next = stddev_curr*2
            security_next = cost_estimating(stddev_next)
            while security_next < security_thres:
                print("while security_curr < security_thres")
                stddev_next = stddev_next*2
                security_next = cost_estimating(stddev_next)
            #     print("testing: (stddev_next, security_next) ", stddev_next, security_next)
            # print("testing: finish loop")
            return binary_search(stddev_curr, stddev_next)
        elif security_curr >  security_thres + 1:
            print("security_curr >  security_thres + 1")
            # print("else")
            stddev_curr /=2
        else:
            print("else")
            return stddev_curr


secret_ternary = ND.Uniform(-1, 1)
# error_gaussian = ND.DiscreteGaussian(stddev, mean=0, n=None)
stddev_list_classical_usvp = []
stddev_list_quantum_usvp = []
cost_model_classic = RC.BDGL16
cost_model_quantum = RC.LaaMosPol14
shape_model="gsa"
estimate_lwe_usvp_classic = partial(LWE.primal_usvp)#, red_shape_model=shape_model, red_cost_model = cost_model_classic)
estimate_lwe_usvp_quantum = partial(LWE.primal_usvp, red_shape_model=shape_model, red_cost_model = cost_model_quantum)
security_thres = 128
margin = 0
for (n_s, logq) in [(630, 32), (1024, 32), (2048, 64), (3072, 64)]:#(630, 32), (1024, 32), 
    print("classical...")
    stddev_list_classical_usvp += [minimal_stddev(estimate_lwe_usvp_classic, n_s, logq, secret_ternary, security_thres + margin, log_stddev_initial = 1)]
    print("quantum...")
    stddev_list_quantum_usvp += [minimal_stddev(estimate_lwe_usvp_quantum, n_s, logq, secret_ternary, security_thres + margin, log_stddev_initial = 1)]
    print("---n = ", n_s, " classical stddev = ", stddev_list_classical_usvp[-1], " quantum stddev = ", stddev_list_quantum_usvp[-1], "---")
print("usvp classical: ", stddev_list_classical_usvp)
print("usvp quantum: ", stddev_list_quantum_usvp)

# n_dim = 2**17 #131072
# logq = 2400
# stddev = 2**9
# secret_ternary = ND.Uniform(-1, 1)
# error_gaussian = ND.DiscreteGaussian(stddev, mean=0, n=None)
# cost_model_classic = RC.LaaMosPol14#RC.MATZOV
# shape_model="gsa"
# instance = LWE.Parameters(n=n_dim, q=2**logq, Xs=secret_ternary, Xe = error_gaussian)

# print(LWE.primal_usvp(instance, red_shape_model="gsa", red_cost_model = RC.LaaMosPol14))