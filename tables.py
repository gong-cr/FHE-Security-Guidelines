import sys
sys.path.insert(1, 'lattice-estimator')
from estimator import *
from estimator.lwe_dual import dual_hybrid
from sage.all import oo, log
from functools import partial

classic_model = RC.BDGL16
quantum_model = RC.LaaMosPol14


# Need to do:
# 1. Update Table numbers
# 2. Cross check Table entries and add:
    # 192/256 for TFHE
    # 2048/4096 for log(Q) schemes
# 3. run the script

# Table 5.1 - 128-bit security, ternary secret
param_1024_ternary_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**26, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_1024_ternary_classic_128"
)

param_1024_ternary_quantum_128 = LWE.Parameters(
    n = 1024,
    q = 2**25,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_1024_ternary_quantum_128"
)
param_2048_ternary_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**54, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_ternary_classic_128"
)

param_2048_ternary_quantum_128 = LWE.Parameters(
    n = 2048,
    q = 2**50,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_ternary_quantum_128"
)

param_4096_ternary_classic_128 = LWE.Parameters(
    n = 4096,
    q = 2**108, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_ternary_classic_128"
)

param_4096_ternary_quantum_128 = LWE.Parameters(
    n = 4096,
    q = 2**101,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_ternary_quantum_128"
)

param_8192_ternary_classic_128 = LWE.Parameters(
    n = 8192,
    q = 2**217, #2**214,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_classic_128"
)

param_8192_ternary_quantum_128 = LWE.Parameters(
    n = 8192,
    q = 2**203,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_quantum_128"
)

param_16384_ternary_classic_128 = LWE.Parameters(
    n = 16384,
    q = 2**438, #438, 2**431,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_classic_128"
)

#TODO: update param_16384_ternary_quantum_128 (121-bits)
param_16384_ternary_quantum_128 = LWE.Parameters(
    n = 16384,
    q = 2**409, # 409 2**410,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_quantum_128"
)

param_32768_ternary_classic_128 = LWE.Parameters(
    n = 32768,
    q = 2**881, #2**867,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_classic_128"
)

param_32768_ternary_quantum_128 = LWE.Parameters(
    n = 32768,
    q = 2**826,#2**823, 825
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_quantum_128"
)

param_65536_ternary_classic_128 = LWE.Parameters(
    n = 65536,
    q = 2**1777, #2**1745, 1775
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_classic_128"
)

param_65536_ternary_quantum_128 = LWE.Parameters(
    n = 65536,
    q = 2**1664, #2**1656,1662
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_quantum_128"
)

param_131072_ternary_classic_128 = LWE.Parameters(
    n = 131072,
    q = 2**3576, #2**3515,3575
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_classic_128"
)

param_131072_ternary_quantum_128 = LWE.Parameters(
    n = 131072,
    q = 2**3348, #3337,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_quantum_128"
)

Table_5_1_a = [(param_2048_ternary_classic_128, 128, classic_model),
             (param_2048_ternary_quantum_128, 128, quantum_model),
             (param_4096_ternary_classic_128, 128, classic_model),
             (param_4096_ternary_quantum_128, 128, quantum_model),
             (param_8192_ternary_classic_128, 128, classic_model),
             (param_8192_ternary_quantum_128, 128, quantum_model),
             (param_16384_ternary_classic_128, 128, classic_model),
             (param_16384_ternary_quantum_128, 128, quantum_model),
             (param_32768_ternary_classic_128, 128, classic_model),
             (param_32768_ternary_quantum_128, 128, quantum_model),
             (param_65536_ternary_classic_128, 128, classic_model),
             (param_65536_ternary_quantum_128, 128, quantum_model),
             (param_131072_ternary_classic_128, 128, classic_model),
             (param_131072_ternary_quantum_128, 128, quantum_model)] 

# Table 5.1 - 192-bit security, ternary secret

param_2048_ternary_classic_192 = LWE.Parameters(
    n = 2048,
    q = 2**37, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_ternary_classic_192"
)

param_2048_ternary_quantum_192 = LWE.Parameters(
    n = 2048,
    q = 2**34,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_ternary_quantum_192"
)

param_4096_ternary_classic_192 = LWE.Parameters(
    n = 4096,
    q = 2**75, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_ternary_classic_192"
)

param_4096_ternary_quantum_192 = LWE.Parameters(
    n = 4096,
    q = 2**70,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_ternary_quantum_192"
)

param_8192_ternary_classic_192 = LWE.Parameters(
    n = 8192,
    q = 2**151, #2**148,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_classic_192"
)

param_8192_ternary_quantum_192 = LWE.Parameters(
    n = 8192,
    q = 2**141,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_quantum_192"
)

param_16384_ternary_classic_192 = LWE.Parameters(
    n = 16384,
    q = 2**304,#2**297,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_classic_192"
)

param_16384_ternary_quantum_192 = LWE.Parameters(
    n = 16384,
    q = 2**283, #2**283,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_quantum_192"
)

param_32768_ternary_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**611, #2**596,610
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_classic_192"
)

param_32768_ternary_quantum_192 = LWE.Parameters(
    n = 32768,
    q = 2**570, #2**570,569
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_quantum_192"
)

param_65536_ternary_classic_192 = LWE.Parameters(
    n = 65536,
    q = 2**1229,#2**1196,1225
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_classic_192"
)

param_65536_ternary_quantum_192 = LWE.Parameters(
    n = 65536,
    q = 2**1145,#1143
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_quantum_192"
)

param_131072_ternary_classic_192 = LWE.Parameters(
    n = 131072,
    q = 2**2469, #2**2400,2462
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_classic_192"
)

param_131072_ternary_quantum_192 = LWE.Parameters(
    n = 131072,
    q = 2**2302, #2**2296,2300
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_quantum_192"
)

Table_5_1_b = [(param_2048_ternary_classic_192, 192, classic_model),
             (param_2048_ternary_quantum_192, 192, quantum_model),
             (param_4096_ternary_classic_192, 192, classic_model),
             (param_4096_ternary_quantum_192, 192, quantum_model),
             (param_8192_ternary_classic_192, 192, classic_model),
             (param_8192_ternary_quantum_192, 192, quantum_model),
             (param_16384_ternary_classic_192, 192, classic_model),
             (param_16384_ternary_quantum_192, 192, quantum_model),
             (param_32768_ternary_classic_192, 192, classic_model),
             (param_32768_ternary_quantum_192, 192, quantum_model),
             (param_65536_ternary_classic_192, 192, classic_model),
             (param_65536_ternary_quantum_192, 192, quantum_model),
             (param_131072_ternary_classic_192, 192, classic_model),
             (param_131072_ternary_quantum_192, 192, quantum_model)]

# Table 5.1 - 256-bit security, ternary secret

param_2048_ternary_classic_256 = LWE.Parameters(
    n = 2048,
    q = 2**28,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_ternary_classic_256"
)

param_2048_ternary_quantum_256 = LWE.Parameters(
    n = 2048,
    q = 2**26,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_ternary_quantum_256"
)

param_4096_ternary_classic_256 = LWE.Parameters(
    n = 4096,
    q = 2**58, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_ternary_classic_256"
)

param_4096_ternary_quantum_256 = LWE.Parameters(
    n = 4096,
    q = 2**54, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_ternary_quantum_256"
)

param_8192_ternary_classic_256 = LWE.Parameters(
    n = 8192,
    q = 2**117, #2**114,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_classic_256"
)

param_8192_ternary_quantum_256 = LWE.Parameters(
    n = 8192,
    q = 2**109, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_quantum_256"
)

param_16384_ternary_classic_256 = LWE.Parameters(
    n = 16384,
    q = 2**237, #2**230,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_classic_256"
)

param_16384_ternary_quantum_256 = LWE.Parameters(
    n = 16384,
    q = 2**220,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_quantum_256"
)

param_32768_ternary_classic_256 = LWE.Parameters(
    n = 32768,
    q = 2**475, #2**462,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_classic_256"
)

#TODO: update param_32768_ternary_quantum_256 (127-bits)
param_32768_ternary_quantum_256 = LWE.Parameters(
    n = 32768,
    q = 2**442,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_quantum_256"
)

param_65536_ternary_classic_256 = LWE.Parameters(
    n = 65536,
    q = 2**955, #2**927,953
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_classic_256"
)

param_65536_ternary_quantum_256 = LWE.Parameters(
    n = 65536,
    q = 2**889,#887
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_quantum_256"
)

param_131072_ternary_classic_256 = LWE.Parameters(
    n = 131072,
    q = 2**1918, #2**1865,1912
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_classic_256"
)

param_131072_ternary_quantum_256 = LWE.Parameters(
    n = 131072,
    q = 2**1784,#1781 1781
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_quantum_256"
)

Table_5_1_c = [(param_2048_ternary_classic_256, 256, classic_model),
             (param_2048_ternary_quantum_256, 256, quantum_model),
             (param_4096_ternary_classic_256, 256, classic_model),
             (param_4096_ternary_quantum_256, 256, quantum_model),
             (param_8192_ternary_classic_256, 256, classic_model),
             (param_8192_ternary_quantum_256, 256, quantum_model),
             (param_16384_ternary_classic_256, 256, classic_model),
             (param_16384_ternary_quantum_256, 256, quantum_model),
             (param_32768_ternary_classic_256, 256, classic_model),
             (param_32768_ternary_quantum_256, 256, quantum_model),
             (param_65536_ternary_classic_256, 256, classic_model),
             (param_65536_ternary_quantum_256, 256, quantum_model),
             (param_131072_ternary_classic_256, 256, classic_model),
             (param_131072_ternary_quantum_256, 256, quantum_model)]


# Table 5.1 - 128-bit security, gaussian secret
param_1024_gaussian_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**29, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_1024_gaussian_classic_128"
)

param_1024_gaussian_quantum_128 = LWE.Parameters(
    n = 1024,
    q = 2**27,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_gaussian_quantum_128"
)

param_2048_gaussian_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**56, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_gaussian_classic_128"
)

param_2048_gaussian_quantum_128 = LWE.Parameters(
    n = 2048,
    q = 2**52,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_gaussian_quantum_128"
)

param_4096_gaussian_classic_128 = LWE.Parameters(
    n = 4096,
    q = 2**110, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_gaussian_classic_128"
)

param_4096_gaussian_quantum_128 = LWE.Parameters(
    n = 4096,
    q = 2**103,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_gaussian_quantum_128"
)

param_8192_gaussian_classic_128 = LWE.Parameters(
    n = 8192,
    q = 2**219, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_gaussian_classic_128"
)

param_8192_gaussian_quantum_128 = LWE.Parameters(
    n = 8192,
    q = 2**205,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_gaussian_quantum_128"
)

param_16384_gaussian_classic_128 = LWE.Parameters(
    n = 16384,
    q = 2**439,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_gaussian_classic_128"
)

param_16384_gaussian_quantum_128 = LWE.Parameters(
    n = 16384,
    q = 2**411, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_gaussian_quantum_128"
)

param_32768_gaussian_classic_128 = LWE.Parameters(
    n = 32768,
    q = 2**883, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_classic_128"
)

param_32768_gaussian_quantum_128 = LWE.Parameters(
    n = 32768,
    q = 2**828,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_quantum_128"
)

param_65536_gaussian_classic_128 = LWE.Parameters(
    n = 65536,
    q = 2**1779, #2**1745,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_gaussian_classic_128"
)

param_65536_gaussian_quantum_128 = LWE.Parameters(
    n = 65536,
    q = 2**1666, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_gaussian_quantum_128"
)

param_131072_gaussian_classic_128 = LWE.Parameters(
    n = 131072,
    q = 2**3578, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_gaussian_classic_128"
)

param_131072_gaussian_quantum_128 = LWE.Parameters(
    n = 131072,
    q = 2**3351,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_gaussian_quantum_128"
)

Table_5_1_d = [(param_2048_gaussian_classic_128, 128, classic_model),
             (param_2048_gaussian_quantum_128, 128, quantum_model),
             (param_4096_gaussian_classic_128, 128, classic_model),
             (param_4096_gaussian_quantum_128, 128, quantum_model),
             (param_8192_gaussian_classic_128, 128, classic_model),
             (param_8192_gaussian_quantum_128, 128, quantum_model),
             (param_16384_gaussian_classic_128, 128, classic_model),
             (param_16384_gaussian_quantum_128, 128, quantum_model),
             (param_32768_gaussian_classic_128, 128, classic_model),
             (param_32768_gaussian_quantum_128, 128, quantum_model),
             (param_65536_gaussian_classic_128, 128, classic_model),
             (param_65536_gaussian_quantum_128, 128, quantum_model),
             (param_131072_gaussian_classic_128, 128, classic_model),
             (param_131072_gaussian_quantum_128, 128, quantum_model)] 

# Table 5.1 - 192-bit security, gaussian secret

param_2048_gaussian_classic_192 = LWE.Parameters(
    n = 2048,
    q = 2**39, #37
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_gaussian_classic_192"
)

param_2048_gaussian_quantum_192 = LWE.Parameters(
    n = 2048,
    q = 2**36,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_gaussian_quantum_192"
)

param_4096_gaussian_classic_192 = LWE.Parameters(
    n = 4096,
    q = 2**77,#75 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_gaussian_classic_192"
)

param_4096_gaussian_quantum_192 = LWE.Parameters(
    n = 4096,
    q = 2**72,#70
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_gaussian_quantum_192"
)

param_8192_gaussian_classic_192 = LWE.Parameters(
    n = 8192,
    q = 2**153, #2**148,151
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_gaussian_classic_192"
)

param_8192_gaussian_quantum_192 = LWE.Parameters(
    n = 8192,
    q = 2**143,#141
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_gaussian_quantum_192"
)

param_16384_gaussian_classic_192 = LWE.Parameters(
    n = 16384,
    q = 2**306,#304
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_gaussian_classic_192"
)

param_16384_gaussian_quantum_192 = LWE.Parameters(
    n = 16384,
    q = 2**285, #284
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_gaussian_quantum_192"
)

param_32768_gaussian_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**613,#610 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_classic_192"
)

param_32768_gaussian_quantum_192 = LWE.Parameters(
    n = 32768,
    q = 2**572, #569
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_quantum_192"
)

param_65536_gaussian_classic_192 = LWE.Parameters(
    n = 65536,
    q = 2**1231,#1225
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_gaussian_classic_192"
)

param_65536_gaussian_quantum_192 = LWE.Parameters(
    n = 65536,
    q = 2**1147,#1143
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_gaussian_quantum_192"
)

param_131072_gaussian_classic_192 = LWE.Parameters(
    n = 131072,
    q = 2**2471, #2462
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_gaussian_classic_192"
)

param_131072_gaussian_quantum_192 = LWE.Parameters(
    n = 131072,
    q = 2**2304, #2300
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_gaussian_quantum_192"
)

Table_5_1_e = [(param_2048_gaussian_classic_192, 192, classic_model),
             (param_2048_gaussian_quantum_192, 192, quantum_model),
             (param_4096_gaussian_classic_192, 192, classic_model),
             (param_4096_gaussian_quantum_192, 192, quantum_model),
             (param_8192_gaussian_classic_192, 192, classic_model),
             (param_8192_gaussian_quantum_192, 192, quantum_model),
             (param_16384_gaussian_classic_192, 192, classic_model),
             (param_16384_gaussian_quantum_192, 192, quantum_model),
             (param_32768_gaussian_classic_192, 192, classic_model),
             (param_32768_gaussian_quantum_192, 192, quantum_model),
             (param_65536_gaussian_classic_192, 192, classic_model),
             (param_65536_gaussian_quantum_192, 192, quantum_model),
             (param_131072_gaussian_classic_192, 192, classic_model),
             (param_131072_gaussian_quantum_192, 192, quantum_model)]


# Table 5.1 - 256-bit security, gaussian secret

param_2048_gaussian_classic_256 = LWE.Parameters(
    n = 2048,
    q = 2**30,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_gaussian_classic_256"
)

param_2048_gaussian_quantum_256 = LWE.Parameters(
    n = 2048,
    q = 2**28,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_gaussian_quantum_256"
)

param_4096_gaussian_classic_256 = LWE.Parameters(
    n = 4096,
    q = 2**60, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_gaussian_classic_256"
)

param_4096_gaussian_quantum_256 = LWE.Parameters(
    n = 4096,
    q = 2**56, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_gaussian_quantum_256"
)

param_8192_gaussian_classic_256 = LWE.Parameters(
    n = 8192,
    q = 2**119,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_gaussian_classic_256"
)

param_8192_gaussian_quantum_256 = LWE.Parameters(
    n = 8192,
    q = 2**111, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_gaussian_quantum_256"
)

param_16384_gaussian_classic_256 = LWE.Parameters(
    n = 16384,
    q = 2**239,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_gaussian_classic_256"
)

param_16384_gaussian_quantum_256 = LWE.Parameters(
    n = 16384,
    q = 2**222,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_gaussian_quantum_256"
)

param_32768_gaussian_classic_256 = LWE.Parameters(
    n = 32768,
    q = 2**478,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_classic_256"
)

param_32768_gaussian_quantum_256 = LWE.Parameters(
    n = 32768,
    q = 2**445,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_quantum_256"
)

param_65536_gaussian_classic_256 = LWE.Parameters(
    n = 65536,
    q = 2**957, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_gaussian_classic_256"
)

param_65536_gaussian_quantum_256 = LWE.Parameters(
    n = 65536,
    q = 2**891,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_gaussian_quantum_256"
)

param_131072_gaussian_classic_256 = LWE.Parameters(
    n = 131072,
    # looks wrong
    q = 2**1920, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_gaussian_classic_256"
)

param_131072_gaussian_quantum_256 = LWE.Parameters(
    n = 131072,
    # looks wrong
    q = 2**1786,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_gaussian_quantum_256"
)

Table_5_1_f = [(param_2048_gaussian_classic_256, 256, classic_model),
             (param_2048_gaussian_quantum_256, 256, quantum_model),
             (param_4096_gaussian_classic_256, 256, classic_model),
             (param_4096_gaussian_quantum_256, 256, quantum_model),
             (param_8192_gaussian_classic_256, 256, classic_model),
             (param_8192_gaussian_quantum_256, 256, quantum_model),
             (param_16384_gaussian_classic_256, 256, classic_model),
             (param_16384_gaussian_quantum_256, 256, quantum_model),
             (param_32768_gaussian_classic_256, 256, classic_model),
             (param_32768_gaussian_quantum_256, 256, quantum_model),
             (param_65536_gaussian_classic_256, 256, classic_model),
             (param_65536_gaussian_quantum_256, 256, quantum_model),
             (param_131072_gaussian_classic_256, 256, classic_model),
             (param_131072_gaussian_quantum_256, 256, quantum_model)]


# Table 5.3

# q = 2**32

param_tfhe_630_binary_classic_128_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**17.9),
    m = oo,
    tag = "param_tfhe_630_binary_classic_128_32"
)

param_tfhe_630_ternary_classic_128_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**16.6),
    m = oo,
    tag = "param_tfhe_630_ternary_classic_128_32"
)

param_tfhe_630_gaussian_classic_128_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**14.2),
    m = oo,
    tag = "param_tfhe_630_gaussian_classic_128_32"
)

param_tfhe_630_binary_quantum_128_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**18.9),
    m = oo,
    tag = "param_tfhe_630_binary_quantum_128_32"
)

param_tfhe_630_ternary_quantum_128_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**17.7),
    m = oo,
    tag = "param_tfhe_630_ternary_quantum_128_32"
)

param_tfhe_630_gaussian_quantum_128_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**15.4),
    m = oo,
    tag = "param_tfhe_630_gaussian_quantum_128_32"
)

param_tfhe_1024_binary_classic_128_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**7.6),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_128_32"
)

param_tfhe_1024_ternary_classic_128_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**6.3),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_128_32"
)

param_tfhe_1024_gaussian_classic_128_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**4.5),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_128_32"
)

param_tfhe_1024_binary_quantum_128_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**9.2),
    m = oo,
    tag = "param_tfhe_1024_binary_quantum_128_32"
)

param_tfhe_1024_ternary_quantum_128_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**8.0),
    m = oo,
    tag = "param_tfhe_1024_ternary_quantum_128_32"
)

param_tfhe_1024_gaussian_quantum_128_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**6.3),
    m = oo,
    tag = "param_tfhe_1024_gaussian_quantum_128_32"
)

param_tfhe_2048_binary_classic_128_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_2048_binary_classic_128_32"
)

param_tfhe_2048_ternary_classic_128_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_128_32"
)

param_tfhe_2048_gaussian_classic_128_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_128_32"
)

param_tfhe_2048_binary_quantum_128_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_2048_binary_quantum_128_32"
)

param_tfhe_2048_ternary_quantum_128_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_2048_ternary_quantum_128_32"
)

param_tfhe_2048_gaussian_quantum_128_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_2048_gaussian_quantum_128_32"
)



# q = 2**64

param_tfhe_630_binary_classic_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**49.9),
    m = oo,
    tag = "param_tfhe_630_binary_classic_128"
)

param_tfhe_630_ternary_classic_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**48.6),
    m = oo,
    tag = "param_tfhe_630_ternary_classic_128"
)

param_tfhe_630_gaussian_classic_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**46.2),
    m = oo,
    tag = "param_tfhe_630_gaussian_classic_128"
)

param_tfhe_630_binary_quantum_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**50.9),
    m = oo,
    tag = "param_tfhe_630_binary_quantum_128"
)

param_tfhe_630_ternary_quantum_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**49.7),
    m = oo,
    tag = "param_tfhe_630_ternary_quantum_128"
)

param_tfhe_630_gaussian_quantum_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**47.4),
    m = oo,
    tag = "param_tfhe_630_gaussian_quantum_128"
)

param_tfhe_1024_binary_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**39.6),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_128"
)

param_tfhe_1024_ternary_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**38.3),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_128"
)

param_tfhe_1024_gaussian_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**36.1),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_128"
)

param_tfhe_1024_binary_quantum_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**41.2),
    m = oo,
    tag = "param_tfhe_1024_binary_quantum_128"
)

param_tfhe_1024_ternary_quantum_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**40.0),
    m = oo,
    tag = "param_tfhe_1024_ternary_quantum_128"
)

param_tfhe_1024_gaussian_quantum_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**37.9),
    m = oo,
    tag = "param_tfhe_1024_gaussian_quantum_128"
)

param_tfhe_2048_binary_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**12.6),
    m = oo,
    tag = "param_tfhe_2048_binary_classic_128"
)

param_tfhe_2048_ternary_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**11.4),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_128"
)

param_tfhe_2048_gaussian_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**9.4),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_128"
)

param_tfhe_2048_binary_quantum_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**16.0),
    m = oo,
    tag = "param_tfhe_2048_binary_quantum_128"
)

param_tfhe_2048_ternary_quantum_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**14.8),
    m = oo,
    tag = "param_tfhe_2048_ternary_quantum_128"
)

param_tfhe_2048_gaussian_quantum_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**12.7),
    m = oo,
    tag = "param_tfhe_2048_gaussian_quantum_128"
)

param_tfhe_4096_binary_classic_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_binary_classic_128"
)

param_tfhe_4096_ternary_classic_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_ternary_classic_128"
)

param_tfhe_4096_gaussian_classic_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_gaussian_classic_128"
)

param_tfhe_4096_binary_quantum_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_binary_quantum_128"
)

param_tfhe_4096_ternary_quantum_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_ternary_quantum_128"
)

param_tfhe_4096_gaussian_quantum_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_gaussian_quantum_128"
)

Table_5_3_a = [
             (param_tfhe_630_binary_classic_128_32, 128, classic_model),
             (param_tfhe_630_ternary_classic_128_32, 128, classic_model),
             (param_tfhe_630_gaussian_classic_128_32, 128, classic_model),
             (param_tfhe_630_binary_quantum_128_32, 128, quantum_model),
             (param_tfhe_630_ternary_quantum_128_32, 128, quantum_model),
             (param_tfhe_630_gaussian_quantum_128_32, 128, quantum_model),    
             (param_tfhe_1024_binary_classic_128_32, 128, classic_model),
             (param_tfhe_1024_ternary_classic_128_32, 128, classic_model),
             (param_tfhe_1024_gaussian_classic_128_32, 128, classic_model),
             (param_tfhe_1024_binary_quantum_128_32, 128, quantum_model),
             (param_tfhe_1024_ternary_quantum_128_32, 128, quantum_model),
             (param_tfhe_1024_gaussian_quantum_128_32, 128, quantum_model),  
             (param_tfhe_2048_binary_classic_128_32, 128, classic_model),
             (param_tfhe_2048_ternary_classic_128_32, 128, classic_model),
             (param_tfhe_2048_gaussian_classic_128_32, 128, classic_model),
             (param_tfhe_2048_binary_quantum_128_32, 128, quantum_model),
             (param_tfhe_2048_ternary_quantum_128_32, 128, quantum_model),
             (param_tfhe_2048_gaussian_quantum_128_32, 128, quantum_model),      
             (param_tfhe_630_binary_classic_128, 128, classic_model),
             (param_tfhe_630_binary_quantum_128, 128, quantum_model),
             (param_tfhe_630_ternary_classic_128, 128, classic_model),
             (param_tfhe_630_ternary_quantum_128, 128, quantum_model),
             (param_tfhe_630_gaussian_classic_128, 128, classic_model),
             (param_tfhe_630_gaussian_quantum_128, 128, quantum_model),
             (param_tfhe_1024_binary_classic_128, 128, classic_model),
             (param_tfhe_1024_binary_quantum_128, 128, quantum_model),
             (param_tfhe_1024_ternary_classic_128, 128, classic_model),
             (param_tfhe_1024_ternary_quantum_128, 128, quantum_model),
             (param_tfhe_1024_gaussian_classic_128, 128, classic_model),
             (param_tfhe_1024_gaussian_quantum_128, 128, quantum_model),
             (param_tfhe_2048_binary_classic_128, 128, classic_model),
             (param_tfhe_2048_binary_quantum_128, 128, quantum_model),
             (param_tfhe_2048_ternary_classic_128, 128, classic_model),
             (param_tfhe_2048_ternary_quantum_128, 128, quantum_model), 
             (param_tfhe_2048_gaussian_classic_128, 128, classic_model),
             (param_tfhe_2048_gaussian_quantum_128, 128, quantum_model),
             (param_tfhe_4096_binary_classic_128, 128, classic_model),
             (param_tfhe_4096_binary_quantum_128, 128, quantum_model),
             (param_tfhe_4096_ternary_classic_128, 128, classic_model),
             (param_tfhe_4096_ternary_quantum_128, 128, quantum_model),
             (param_tfhe_4096_gaussian_classic_128, 128, classic_model),
             (param_tfhe_4096_gaussian_quantum_128, 128, quantum_model)]


# q = 2**32

param_tfhe_630_binary_classic_192_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**23.6),
    m = oo,
    tag = "param_tfhe_630_binary_classic_192_32"
)

param_tfhe_630_ternary_classic_192_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**22.2),
    m = oo,
    tag = "param_tfhe_630_ternary_classic_192_32"
)

param_tfhe_630_gaussian_classic_192_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**19.7),
    m = oo,
    tag = "param_tfhe_630_gaussian_classic_192_32"
)

param_tfhe_630_binary_quantum_192_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**24.3),
    m = oo,
    tag = "param_tfhe_630_binary_quantum_192_32"
)

param_tfhe_630_ternary_quantum_192_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**23.0),
    m = oo,
    tag = "param_tfhe_630_ternary_quantum_192_32"
)

param_tfhe_630_gaussian_quantum_192_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**20.6),
    m = oo,
    tag = "param_tfhe_630_gaussian_quantum_192_32"
)

param_tfhe_1024_binary_classic_192_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**16.3),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_192_32"
)

param_tfhe_1024_ternary_classic_192_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**15.0),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_192_32"
)

param_tfhe_1024_gaussian_classic_192_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**12.4),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_192_32"
)

param_tfhe_1024_binary_quantum_192_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**17.5),
    m = oo,
    tag = "param_tfhe_1024_binary_quantum_192_32"
)

param_tfhe_1024_ternary_quantum_192_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**16.2),
    m = oo,
    tag = "param_tfhe_1024_ternary_quantum_192_32"
)

param_tfhe_1024_gaussian_quantum_192_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**13.8),
    m = oo,
    tag = "param_tfhe_1024_gaussian_quantum_192_32"
)

param_tfhe_2048_binary_classic_192_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(4),
    m = oo,
    tag = "param_tfhe_2048_binary_classic_192_32"
)

param_tfhe_2048_ternary_classic_192_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(4),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_192_32"
)

param_tfhe_2048_gaussian_classic_192_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(4),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_192_32"
)

param_tfhe_2048_binary_quantum_192_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(4),
    m = oo,
    tag = "param_tfhe_2048_binary_quantum_192_32"
)

param_tfhe_2048_ternary_quantum_192_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(4),
    m = oo,
    tag = "param_tfhe_2048_ternary_quantum_192_32"
)

param_tfhe_2048_gaussian_quantum_192_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(4),
    m = oo,
    tag = "param_tfhe_2048_gaussian_quantum_192_32"
)

# q = 2**64

param_tfhe_630_binary_classic_192 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**55.6),
    m = oo,
    tag = "param_tfhe_630_binary_classic_192"
)

param_tfhe_630_ternary_classic_192 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**54.2),
    m = oo,
    tag = "param_tfhe_630_ternary_classic_192"
)

param_tfhe_630_gaussian_classic_192 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**51.7),
    m = oo,
    tag = "param_tfhe_630_gaussian_classic_192"
)

param_tfhe_630_binary_quantum_192 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**56.3),
    m = oo,
    tag = "param_tfhe_630_binary_quantum_192"
)

param_tfhe_630_ternary_quantum_192 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**55.0),
    m = oo,
    tag = "param_tfhe_630_ternary_quantum_192"
)

param_tfhe_630_gaussian_quantum_192 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**52.6),
    m = oo,
    tag = "param_tfhe_630_gaussian_quantum_192"
)

param_tfhe_1024_binary_classic_192 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**48.3),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_192"
)

param_tfhe_1024_ternary_classic_192 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**47.0),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_192"
)

param_tfhe_1024_gaussian_classic_192 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**44.4),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_192"
)

param_tfhe_1024_binary_quantum_192 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**49.5),
    m = oo,
    tag = "param_tfhe_1024_binary_quantum_192"
)

param_tfhe_1024_ternary_quantum_192 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**48.2),
    m = oo,
    tag = "param_tfhe_1024_ternary_quantum_192"
)

param_tfhe_1024_gaussian_quantum_192 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**45.8),
    m = oo,
    tag = "param_tfhe_1024_gaussian_quantum_192"
)

param_tfhe_2048_binary_classic_192 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**29.4),
    m = oo,
    tag = "param_tfhe_2048_binary_classic_192"
)

param_tfhe_2048_ternary_classic_192 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**28.1),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_192"
)

param_tfhe_2048_gaussian_classic_192 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**25.5),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_192"
)

param_tfhe_2048_binary_quantum_192 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**31.9),
    m = oo,
    tag = "param_tfhe_2048_binary_quantum_192"
)

param_tfhe_2048_ternary_quantum_192 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**30.6),
    m = oo,
    tag = "param_tfhe_2048_ternary_quantum_192"
)

param_tfhe_2048_gaussian_quantum_192 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**28.2),
    m = oo,
    tag = "param_tfhe_2048_gaussian_quantum_192"
)

param_tfhe_4096_binary_classic_192 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_binary_classic_192"
)

param_tfhe_4096_ternary_classic_192 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_ternary_classic_192"
)

param_tfhe_4096_gaussian_classic_192 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_gaussian_classic_192"
)

param_tfhe_4096_binary_quantum_192 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_binary_quantum_192"
)

param_tfhe_4096_ternary_quantum_192 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_ternary_quantum_192"
)

param_tfhe_4096_gaussian_quantum_192 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_gaussian_quantum_192"
)

Table_5_3_b = [
             (param_tfhe_630_binary_classic_192_32, 192, classic_model),
             (param_tfhe_630_binary_quantum_192_32, 192, quantum_model),
             (param_tfhe_630_ternary_classic_192_32, 192, classic_model),
             (param_tfhe_630_ternary_quantum_192_32, 192, quantum_model),
             (param_tfhe_630_gaussian_classic_192_32, 192, classic_model),
             (param_tfhe_630_gaussian_quantum_192_32, 192, quantum_model),
             (param_tfhe_1024_binary_classic_192_32, 192, classic_model),
             (param_tfhe_1024_binary_quantum_192_32, 192, quantum_model),
             (param_tfhe_1024_ternary_classic_192_32, 192, classic_model),
             (param_tfhe_1024_ternary_quantum_192_32, 192, quantum_model),
             (param_tfhe_1024_gaussian_classic_192_32, 192, classic_model),
             (param_tfhe_1024_gaussian_quantum_192_32, 192, quantum_model),
             (param_tfhe_2048_binary_classic_192_32, 192, classic_model),
             (param_tfhe_2048_binary_quantum_192_32, 192, quantum_model),
             (param_tfhe_2048_ternary_classic_192_32, 192, classic_model),
             (param_tfhe_2048_ternary_quantum_192_32, 192, quantum_model), 
             (param_tfhe_2048_gaussian_classic_192_32, 192, classic_model),
             (param_tfhe_2048_gaussian_quantum_192_32, 192, quantum_model),       
             (param_tfhe_630_binary_classic_192, 192, classic_model),
             (param_tfhe_630_binary_quantum_192, 192, quantum_model),
             (param_tfhe_630_ternary_classic_192, 192, classic_model),
             (param_tfhe_630_ternary_quantum_192, 192, quantum_model),
             (param_tfhe_630_gaussian_classic_192, 192, classic_model),
             (param_tfhe_630_gaussian_quantum_192, 192, quantum_model),
             (param_tfhe_1024_binary_classic_192, 192, classic_model),
             (param_tfhe_1024_binary_quantum_192, 192, quantum_model),
             (param_tfhe_1024_ternary_classic_192, 192, classic_model),
             (param_tfhe_1024_ternary_quantum_192, 192, quantum_model),
             (param_tfhe_1024_gaussian_classic_192, 192, classic_model),
             (param_tfhe_1024_gaussian_quantum_192, 192, quantum_model),
             (param_tfhe_2048_binary_classic_192, 192, classic_model),
             (param_tfhe_2048_binary_quantum_192, 192, quantum_model),
             (param_tfhe_2048_ternary_classic_192, 192, classic_model),
             (param_tfhe_2048_ternary_quantum_192, 192, quantum_model), 
             (param_tfhe_2048_gaussian_classic_192, 192, classic_model),
             (param_tfhe_2048_gaussian_quantum_192, 192, quantum_model),
             (param_tfhe_4096_binary_classic_192, 192, classic_model),
             (param_tfhe_4096_binary_quantum_192, 192, quantum_model),
             (param_tfhe_4096_ternary_classic_192, 192, classic_model),
             (param_tfhe_4096_ternary_quantum_192, 192, quantum_model),
             (param_tfhe_4096_gaussian_classic_192, 192, classic_model),
             (param_tfhe_4096_gaussian_quantum_192, 192, quantum_model)]

# q = 2**32

param_tfhe_1024_binary_classic_256_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**21.0),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_256_32"
)

param_tfhe_1024_ternary_classic_256_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**19.6),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_256_32"
)

param_tfhe_1024_gaussian_classic_256_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**16.9),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_256_32"
)

param_tfhe_1024_binary_quantum_256_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**21.9),
    m = oo,
    tag = "param_tfhe_1024_binary_quantum_256_32"
)

param_tfhe_1024_ternary_quantum_256_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**20.6),
    m = oo,
    tag = "param_tfhe_1024_ternary_quantum_256_32"
)

param_tfhe_1024_gaussian_quantum_256_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**18.1),
    m = oo,
    tag = "param_tfhe_1024_gaussian_quantum_256_32"
)

# q = 2**64

param_tfhe_1024_binary_classic_256 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**53.0),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_256"
)

param_tfhe_1024_ternary_classic_256 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**51.6),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_256"
)

param_tfhe_1024_gaussian_classic_256 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**48.9),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_256"
)

param_tfhe_1024_binary_quantum_256 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**53.9),
    m = oo,
    tag = "param_tfhe_1024_binary_quantum_256"
)

param_tfhe_1024_ternary_quantum_256 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**52.6),
    m = oo,
    tag = "param_tfhe_1024_ternary_quantum_256"
)

param_tfhe_1024_gaussian_quantum_256 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**50.1),
    m = oo,
    tag = "param_tfhe_1024_gaussian_quantum_256"
)

param_tfhe_2048_binary_classic_256 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**38.2),
    m = oo,
    tag = "param_tfhe_2048_binary_classic_256"
)

param_tfhe_2048_ternary_classic_256 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**36.8),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_256"
)

param_tfhe_2048_gaussian_classic_256 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**34.1),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_256"
)

param_tfhe_2048_binary_quantum_256 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**40.1),
    m = oo,
    tag = "param_tfhe_2048_binary_quantum_256"
)

param_tfhe_2048_ternary_quantum_256 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**38.8),
    m = oo,
    tag = "param_tfhe_2048_ternary_quantum_256"
)

param_tfhe_2048_gaussian_quantum_256 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**36.3),
    m = oo,
    tag = "param_tfhe_2048_gaussian_quantum_256"
)

param_tfhe_4096_binary_classic_256 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**8.6),
    m = oo,
    tag = "param_tfhe_4096_binary_classic_256"
)

param_tfhe_4096_ternary_classic_256 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**7.2),
    m = oo,
    tag = "param_tfhe_4096_ternary_classic_256"
)

param_tfhe_4096_gaussian_classic_256 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**4.5),
    m = oo,
    tag = "param_tfhe_4096_gaussian_classic_256"
)

param_tfhe_4096_binary_quantum_256 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**12.5),
    m = oo,
    tag = "param_tfhe_4096_binary_quantum_256"
)

param_tfhe_4096_ternary_quantum_256 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**11.3),
    m = oo,
    tag = "param_tfhe_4096_ternary_quantum_256"
)

param_tfhe_4096_gaussian_quantum_256 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**8.8),
    m = oo,
    tag = "param_tfhe_4096_gaussian_quantum_256"
)

param_tfhe_8192_binary_quantum_256 = LWE.Parameters(
    n = 8192,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2),
    m = oo,
    tag = "param_tfhe_8192_binary_quantum_256"
)


Table_5_3_c = [
            (param_tfhe_1024_binary_classic_256_32, 256, classic_model),
             (param_tfhe_1024_binary_quantum_256_32, 256, quantum_model),
             (param_tfhe_1024_ternary_classic_256_32, 256, classic_model),
             (param_tfhe_1024_ternary_quantum_256_32, 256, quantum_model),
             (param_tfhe_1024_gaussian_classic_256_32, 256, classic_model),
             (param_tfhe_1024_gaussian_quantum_256_32, 256, quantum_model),
             (param_tfhe_1024_binary_classic_256, 256, classic_model),
             (param_tfhe_1024_binary_quantum_256, 256, quantum_model),
             (param_tfhe_1024_ternary_classic_256, 256, classic_model),
             (param_tfhe_1024_ternary_quantum_256, 256, quantum_model),
             (param_tfhe_1024_gaussian_classic_256, 256, classic_model),
             (param_tfhe_1024_gaussian_quantum_256, 256, quantum_model),
             (param_tfhe_2048_binary_classic_256, 256, classic_model),
             (param_tfhe_2048_binary_quantum_256, 256, quantum_model),
             (param_tfhe_2048_ternary_classic_256, 256, classic_model),
             (param_tfhe_2048_ternary_quantum_256, 256, quantum_model), 
             (param_tfhe_2048_gaussian_classic_256, 256, classic_model),
             (param_tfhe_2048_gaussian_quantum_256, 256, quantum_model),
             (param_tfhe_4096_binary_classic_256, 256, classic_model),
             (param_tfhe_4096_binary_quantum_256, 256, quantum_model),
             (param_tfhe_4096_ternary_classic_256, 256, classic_model),
             (param_tfhe_4096_ternary_quantum_256, 256, quantum_model),
             (param_tfhe_4096_gaussian_classic_256, 256, classic_model),
             (param_tfhe_4096_gaussian_quantum_256, 256, quantum_model),
             (param_tfhe_8192_binary_quantum_256, 256, quantum_model)]


with open(output_file, "w") as file, open(params_update_file, "w") as update_file, open(level_diff_file, "w") as diff_file:
    for (param, security_level, model) in all_security_params:
        # if param.n != 16384*2:#delete
        #     continue #delete

        non_matzov_dual = partial(
                dual_hybrid, red_cost_model=model)

        file.write("parameters = {}\n".format(param.tag))
        print("parameters = {}".format(param.tag))
        # params_to_update = []
        try:
            #usvp_level = LWE.primal_usvp(param, red_cost_model = model)
            #dual_level = LWE.dual_hybrid(param, red_cost_model = model)
            #estimator_level = log(min(usvp_level["rop"], dual_level["rop"]),2)
            # hybrid-decoding
            print("param.n  = {}".format(param.n))
            if param.n <= 16384: #param.n == 16384*2
                est = LWE.estimate(param, red_cost_model = model, deny_list = ("arora-gb", "bkw", "dual_hybrid"))
                print("EST = {}".format(est))
                est_dual = non_matzov_dual(param, red_cost_model=model)
                print("EST-dual = {}".format(est_dual))
            else: 
                # check function name
                est = LWE.estimate(param, red_cost_model = model, deny_list = ("arora-gb", "bkw", "dual_hybrid"))
                est_dual = non_matzov_dual(param, red_cost_model=model)
                print("EST-dual = {}".format(est_dual))
                print("EST = {}".format(est))

            file.write("{}\n".format(est))
            file.write("{}\n".format(est_dual))
            costs = []
            costs_no_bdd_hybrid = [] #bdd
            for key in est.keys():
                cost = est[key]["rop"]
                costs.append(cost)
                if key != "bdd_hybrid":  # Exclude 'bdd_hybrid' cost #bdd
                    costs_no_bdd_hybrid.append(cost) #bdd
            costs.append(est_dual["rop"])
            estimator_level = log(min(costs),2)

            if param.n <= 16384: 
                bdd_hybrid_level = log(est["bdd_hybrid"]["rop"],2)
                estimator_level_no_bdd_hybrid = log(min(costs_no_bdd_hybrid), 2)
                diff_file.write("{}, {}, {}, {}, {}, {}\n".format(param.n, estimator_level_no_bdd_hybrid - bdd_hybrid_level, estimator_level_no_bdd_hybrid, bdd_hybrid_level, param.tag, estimator_level))
            if security_level > estimator_level:
                file.write("target security level = {}\n".format(security_level))
                file.write("attained security level = {}\n".format(estimator_level))
                update_file.write("{},{}\n".format(param.tag, estimator_level))
            else:
                file.write("pass.\n")
        except Exception as e:
            print(e)
            file.write("{}\n".format(e))
            file.write("fail.\n")
        file.flush()
        update_file.flush()
        diff_file.flush()

print("COMPLETE")
# file.write("Parameters to update: {}\n".format(params_to_update))