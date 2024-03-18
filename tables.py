import sys
sys.path.insert(1, 'lattice-estimator')
from estimator import *
from estimator.lwe_dual import dual_hybrid
from sage.all import oo, log
from functools import partial

classic_model = RC.BDGL16
quantum_model = RC.LaaMosPol14


# Table 5.2 - 128-bit security, ternary secret
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

param_16384_ternary_quantum_128 = LWE.Parameters(
    n = 16384,
    q = 2**409, 
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
    q = 2**825,#2**823, 825
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_quantum_128"
)

param_65536_ternary_classic_128 = LWE.Parameters(
    n = 65536,
    q = 2**1776, #2**1745, 1775
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_classic_128"
)

param_65536_ternary_quantum_128 = LWE.Parameters(
    n = 65536,
    q = 2**1663, 
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
    q = 2**827,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_quantum_128"
)

param_65536_gaussian_classic_128 = LWE.Parameters(
    n = 65536,
    q = 2**1778, #2**1745,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_gaussian_classic_128"
)

param_65536_gaussian_quantum_128 = LWE.Parameters(
    n = 65536,
    q = 2**1665, 
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
    q = 2**1230,#1225
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
    q = 2**477,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_classic_256"
)

param_32768_gaussian_quantum_256 = LWE.Parameters(
    n = 32768,
    q = 2**444,
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
    q = 2**890,
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

param_tfhe_750_binary_classic_128 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**46.8),
    m = oo,
    tag = "param_tfhe_750_binary_classic_128"
)

param_tfhe_750_ternary_classic_128 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**45.5),
    m = oo,
    tag = "param_tfhe_750_ternary_classic_128"
)

param_tfhe_750_gaussian_classic_128 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**43.0),
    m = oo,
    tag = "param_tfhe_750_gaussian_classic_128"
)

param_tfhe_750_binary_quantum_128 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**48.0),
    m = oo,
    tag = "param_tfhe_750_binary_quantum_128"
)

param_tfhe_750_ternary_quantum_128 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**46.7),
    m = oo,
    tag = "param_tfhe_750_ternary_quantum_128"
)

param_tfhe_750_gaussian_quantum_128 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**44.4),
    m = oo,
    tag = "param_tfhe_750_gaussian_quantum_128"
)

param_tfhe_870_binary_classic_128 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**43.7),
    m = oo,
    tag = "param_tfhe_870_binary_classic_128"
)

param_tfhe_870_ternary_classic_128 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**42.4),
    m = oo,
    tag = "param_tfhe_870_ternary_classic_128"
)

param_tfhe_870_gaussian_classic_128 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**39.9),
    m = oo,
    tag = "param_tfhe_870_gaussian_classic_128"
)

param_tfhe_870_binary_quantum_128 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**45.0),
    m = oo,
    tag = "param_tfhe_870_binary_quantum_128"
)

param_tfhe_870_ternary_quantum_128 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**43.8),
    m = oo,
    tag = "param_tfhe_870_ternary_quantum_128"
)

param_tfhe_870_gaussian_quantum_128 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**41.4),
    m = oo,
    tag = "param_tfhe_870_gaussian_quantum_128"
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

Table_5_2_a = [
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
             (param_tfhe_750_binary_classic_128, 128, classic_model),
             (param_tfhe_750_binary_quantum_128, 128, quantum_model),
             (param_tfhe_750_ternary_classic_128, 128, classic_model),
             (param_tfhe_750_ternary_quantum_128, 128, quantum_model),
             (param_tfhe_750_gaussian_classic_128, 128, classic_model),
             (param_tfhe_750_gaussian_quantum_128, 128, quantum_model),
             (param_tfhe_870_binary_classic_128, 128, classic_model),
             (param_tfhe_870_binary_quantum_128, 128, quantum_model),
             (param_tfhe_870_ternary_classic_128, 128, classic_model),
             (param_tfhe_870_ternary_quantum_128, 128, quantum_model),
             (param_tfhe_870_gaussian_classic_128, 128, classic_model),
             (param_tfhe_870_gaussian_quantum_128, 128, quantum_model),
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


param_tfhe_750_binary_classic_192 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**53.4),
    m = oo,
    tag = "param_tfhe_750_binary_classic_192"
)

param_tfhe_750_ternary_classic_192 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**52.0),
    m = oo,
    tag = "param_tfhe_750_ternary_classic_192"
)

param_tfhe_750_gaussian_classic_192 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**49.5),
    m = oo,
    tag = "param_tfhe_750_gaussian_classic_192"
)

param_tfhe_750_binary_quantum_192 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**54.2),
    m = oo,
    tag = "param_tfhe_750_binary_quantum_192"
)

param_tfhe_750_ternary_quantum_192 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**52.9),
    m = oo,
    tag = "param_tfhe_750_ternary_quantum_192"
)

param_tfhe_750_gaussian_quantum_192 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**50.5),
    m = oo,
    tag = "param_tfhe_750_gaussian_quantum_192"
)

param_tfhe_870_binary_classic_192 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**51.2),
    m = oo,
    tag = "param_tfhe_870_binary_classic_192"
)

param_tfhe_870_ternary_classic_192 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**49.8),
    m = oo,
    tag = "param_tfhe_870_ternary_classic_192"
)

param_tfhe_870_gaussian_classic_192 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**47.3),
    m = oo,
    tag = "param_tfhe_870_gaussian_classic_192"
)

param_tfhe_870_binary_quantum_192 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**52.2),
    m = oo,
    tag = "param_tfhe_870_binary_quantum_192"
)

param_tfhe_870_ternary_quantum_192 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**50.9),
    m = oo,
    tag = "param_tfhe_870_ternary_quantum_128"
)

param_tfhe_870_gaussian_quantum_192 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**48.5),
    m = oo,
    tag = "param_tfhe_870_gaussian_quantum_192"
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

Table_5_2_b = [
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
             (param_tfhe_750_binary_classic_192, 192, classic_model),
             (param_tfhe_750_binary_quantum_192, 192, quantum_model),
             (param_tfhe_750_ternary_classic_192, 192, classic_model),
             (param_tfhe_750_ternary_quantum_192, 192, quantum_model),
             (param_tfhe_750_gaussian_classic_192, 192, classic_model),
             (param_tfhe_750_gaussian_quantum_192, 192, quantum_model),
             (param_tfhe_870_binary_classic_192, 192, classic_model),
             (param_tfhe_870_binary_quantum_192, 192, quantum_model),
             (param_tfhe_870_ternary_classic_192, 192, classic_model),
             (param_tfhe_870_ternary_quantum_192, 192, quantum_model),
             (param_tfhe_870_gaussian_classic_192, 192, classic_model),
             (param_tfhe_870_gaussian_quantum_192, 192, quantum_model),
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


param_tfhe_2048_binary_classic_256_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**6.2),
    m = oo,
    tag = "param_tfhe_2048_binary_classic_256_32"
)

param_tfhe_2048_ternary_classic_256_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**4.8),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_256_32"
)

param_tfhe_2048_gaussian_classic_256_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**2.4),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_256_32"
)

param_tfhe_2048_binary_quantum_256_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**8.1),
    m = oo,
    tag = "param_tfhe_2048_binary_quantum_256_32"
)

param_tfhe_2048_ternary_quantum_256_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**6.8),
    m = oo,
    tag = "param_tfhe_2048_ternary_quantum_256_32"
)

param_tfhe_2048_gaussian_quantum_256_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**4.6),
    m = oo,
    tag = "param_tfhe_2048_gaussian_quantum_256_32"
)

param_tfhe_4096_binary_quantum_256_32 = LWE.Parameters(
    n = 4096,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2),
    m = oo,
    tag = "param_tfhe_4096_binary_quantum_256_32"
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
    Xe = ND.DiscreteGaussian(2**34.2),
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
    Xe = ND.DiscreteGaussian(2**4.8),
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
    Xe = ND.DiscreteGaussian(2**8.9),
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


Table_5_2_c = [
            (param_tfhe_1024_binary_classic_256_32, 256, classic_model),
             (param_tfhe_1024_binary_quantum_256_32, 256, quantum_model),
             (param_tfhe_1024_ternary_classic_256_32, 256, classic_model),
             (param_tfhe_1024_ternary_quantum_256_32, 256, quantum_model),
             (param_tfhe_1024_gaussian_classic_256_32, 256, classic_model),
             (param_tfhe_1024_gaussian_quantum_256_32, 256, quantum_model),
             (param_tfhe_2048_binary_classic_256_32, 256, classic_model),
             (param_tfhe_2048_binary_quantum_256_32, 256, quantum_model),
             (param_tfhe_2048_ternary_classic_256_32, 256, classic_model),
             (param_tfhe_2048_ternary_quantum_256_32, 256, quantum_model),
             (param_tfhe_2048_gaussian_classic_256_32, 256, classic_model),
             (param_tfhe_2048_gaussian_quantum_256_32, 256, quantum_model),
             (param_tfhe_4096_binary_quantum_256_32, 256, quantum_model),
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

Tables = [Table_5_1_a,
          Table_5_1_b,
          Table_5_1_c,
          Table_5_1_d,
          Table_5_1_e,
          Table_5_1_f,
          Table_5_2_a,
          Table_5_2_b,
          Table_5_2_c]

def test_it(param, sec):

    rops = []
    try:
        est1 = LWE.primal_usvp(param[0], red_cost_model = param[2])
        rops.append(est1["rop"])
    except:
        pass
    try:
        est2 = LWE.primal_bdd(param[0], red_cost_model = param[2])
        rops.append(est2["rop"])
    except:
        pass
    try:
        est3 = dh(param[0], red_cost_model = param[2])
        rops.append(est3["rop"])
    except:
        pass

    if log(min(rops),2) < sec:
        print("parameter set {} needs updating".format(param))
        print("the stddev is {}".format(log(param[0].Xe.stddev,2)))
        print("logq is: {}".format(log(param[0].q,2)))
    
    return 0


def test_all_tables():
    for table in Tables:
        for param in table:
            test_it(param, param[1])
    return 0

test_all_tables()