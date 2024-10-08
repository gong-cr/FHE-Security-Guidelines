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

param_2048_ternary_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**53, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_ternary_classic_128"
)

param_4096_ternary_classic_128 = LWE.Parameters(
    n = 4096,
    q = 2**106, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_ternary_classic_128"
)

param_8192_ternary_classic_128 = LWE.Parameters(
    n = 8192,
    q = 2**214,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_classic_128"
)

param_16384_ternary_classic_128 = LWE.Parameters(
    n = 16384,
    q = 2**430,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_classic_128"
)

param_32768_ternary_classic_128 = LWE.Parameters(
    n = 32768,
    q = 2**868,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_classic_128"
)

param_65536_ternary_classic_128 = LWE.Parameters(
    n = 65536,
    q = 2**1747, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_classic_128"
)

param_131072_ternary_classic_128 = LWE.Parameters(
    n = 131072,
    q = 2**3523,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_classic_128"
)

Table_5_2_a = [(param_2048_ternary_classic_128, 128, classic_model),
             (param_4096_ternary_classic_128, 128, classic_model),
             (param_8192_ternary_classic_128, 128, classic_model),
             (param_16384_ternary_classic_128, 128, classic_model),
             (param_32768_ternary_classic_128, 128, classic_model),
             (param_65536_ternary_classic_128, 128, classic_model),
             (param_131072_ternary_classic_128, 128, classic_model)]

# Table 5.2 - 192-bit security, ternary secret

param_2048_ternary_classic_192 = LWE.Parameters(
    n = 2048,
    q = 2**36, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_ternary_classic_192"
)

param_4096_ternary_classic_192 = LWE.Parameters(
    n = 4096,
    q = 2**73, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_ternary_classic_192"
)

param_8192_ternary_classic_192 = LWE.Parameters(
    n = 8192,
    q = 2**147, #2**148,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_classic_192"
)

param_16384_ternary_classic_192 = LWE.Parameters(
    n = 16384,
    q = 2**297,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_classic_192"
)

param_32768_ternary_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**597,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_classic_192"
)

param_65536_ternary_classic_192 = LWE.Parameters(
    n = 65536,
    q = 2**1199,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_classic_192"
)

param_131072_ternary_classic_192 = LWE.Parameters(
    n = 131072,
    q = 2**2411,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_classic_192"
)

Table_5_2_b = [(param_2048_ternary_classic_192, 192, classic_model),
             (param_4096_ternary_classic_192, 192, classic_model),
             (param_8192_ternary_classic_192, 192, classic_model),
             (param_16384_ternary_classic_192, 192, classic_model),
             (param_32768_ternary_classic_192, 192, classic_model),
             (param_65536_ternary_classic_192, 192, classic_model),
             (param_131072_ternary_classic_192, 192, classic_model)]

# Table 5.2 - 256-bit security, ternary secret

param_2048_ternary_classic_256 = LWE.Parameters(
    n = 2048,
    q = 2**27,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_ternary_classic_256"
)

param_4096_ternary_classic_256 = LWE.Parameters(
    n = 4096,
    q = 2**56, 
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_ternary_classic_256"
)

param_8192_ternary_classic_256 = LWE.Parameters(
    n = 8192,
    q = 2**114,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_classic_256"
)

param_16384_ternary_classic_256 = LWE.Parameters(
    n = 16384,
    q = 2**230,,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_classic_256"
)

param_32768_ternary_classic_256 = LWE.Parameters(
    n = 32768,
    q = 2**462,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_classic_256"
)

param_65536_ternary_classic_256 = LWE.Parameters(
    n = 65536,
    q = 2**929,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_classic_256"
)

param_131072_ternary_classic_256 = LWE.Parameters(
    n = 131072,
    q = 2**1866,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_classic_256"
)

Table_5_2_c = [(param_2048_ternary_classic_256, 256, classic_model),
             (param_4096_ternary_classic_256, 256, classic_model),
             (param_8192_ternary_classic_256, 256, classic_model),
             (param_16384_ternary_classic_256, 256, classic_model),
             (param_32768_ternary_classic_256, 256, classic_model),
             (param_65536_ternary_classic_256, 256, classic_model),
             (param_131072_ternary_classic_256, 256, classic_model)]


# Table 5.2 - 128-bit security, gaussian secret (sd = 3.19)
param_1024_gaussian_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**28, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_1024_gaussian_classic_128"
)

param_2048_gaussian_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**55, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_gaussian_classic_128"
)

param_4096_gaussian_classic_128 = LWE.Parameters(
    n = 4096,
    q = 2**108, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_gaussian_classic_128"
)

param_8192_gaussian_classic_128 = LWE.Parameters(
    n = 8192,
    q = 2**216, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_gaussian_classic_128"
)

param_16384_gaussian_classic_128 = LWE.Parameters(
    n = 16384,
    q = 2**432,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_gaussian_classic_128"
)

param_32768_gaussian_classic_128 = LWE.Parameters(
    n = 32768,
    q = 2**870, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_classic_128"
)

param_65536_gaussian_classic_128 = LWE.Parameters(
    n = 65536,
    q = 2**1749,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_gaussian_classic_128"
)

param_131072_gaussian_classic_128 = LWE.Parameters(
    n = 131072,
    q = 2**3523, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_gaussian_classic_128"
)

Table_5_2_d = [(param_2048_gaussian_classic_128, 128, classic_model),
             (param_4096_gaussian_classic_128, 128, classic_model),
             (param_8192_gaussian_classic_128, 128, classic_model),
             (param_16384_gaussian_classic_128, 128, classic_model),
             (param_32768_gaussian_classic_128, 128, classic_model),
             (param_65536_gaussian_classic_128, 128, classic_model),
             (param_131072_gaussian_classic_128, 128, classic_model)]

# Table 5.2 - 192-bit security, gaussian secret

param_2048_gaussian_classic_192 = LWE.Parameters(
    n = 2048,
    q = 2**38,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_gaussian_classic_192"
)

param_4096_gaussian_classic_192 = LWE.Parameters(
    n = 4096,
    q = 2**75, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_gaussian_classic_192"
)

param_8192_gaussian_classic_192 = LWE.Parameters(
    n = 8192,
    q = 2**149,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_gaussian_classic_192"
)

param_16384_gaussian_classic_192 = LWE.Parameters(
    n = 16384,
    q = 2**299,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_gaussian_classic_192"
)

param_32768_gaussian_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**599,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_classic_192"
)

param_65536_gaussian_classic_192 = LWE.Parameters(
    n = 65536,
    q = 2**1201,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_gaussian_classic_192"
)

param_131072_gaussian_classic_192 = LWE.Parameters(
    n = 131072,
    q = 2**2313,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_gaussian_classic_192"
)

Table_5_2_e = [(param_2048_gaussian_classic_192, 192, classic_model),
             (param_4096_gaussian_classic_192, 192, classic_model),
             (param_8192_gaussian_classic_192, 192, classic_model),
             (param_16384_gaussian_classic_192, 192, classic_model),
             (param_32768_gaussian_classic_192, 192, classic_model),
             (param_65536_gaussian_classic_192, 192, classic_model),
             (param_131072_gaussian_classic_192, 192, classic_model)]


# Table 5.2 - 256-bit security, gaussian secret

param_2048_gaussian_classic_256 = LWE.Parameters(
    n = 2048,
    q = 2**30,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_2048_gaussian_classic_256"
)

param_4096_gaussian_classic_256 = LWE.Parameters(
    n = 4096,
    q = 2**58, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_4096_gaussian_classic_256"
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
    q = 2**116, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_gaussian_quantum_256"
)

param_16384_gaussian_quantum_256 = LWE.Parameters(
    n = 16384,
    q = 2**232,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_gaussian_quantum_256"
)

param_32768_gaussian_classic_256 = LWE.Parameters(
    n = 32768,
    q = 2**464,
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_gaussian_classic_256"
)

param_65536_gaussian_classic_256 = LWE.Parameters(
    n = 65536,
    q = 2**931, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_gaussian_classic_256"
)

param_131072_gaussian_classic_256 = LWE.Parameters(
    n = 131072,
    q = 2**1868, 
    Xs = ND.DiscreteGaussian(3.19),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_gaussian_classic_256"
)

Table_5_2_f = [(param_2048_gaussian_classic_256, 256, classic_model),
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
    Xe = ND.DiscreteGaussian(2**18.5),
    m = oo,
    tag = "param_tfhe_630_binary_classic_128_32"
)

param_tfhe_630_ternary_classic_128_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**17.2),
    m = oo,
    tag = "param_tfhe_630_ternary_classic_128_32"
)

param_tfhe_630_gaussian_classic_128_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**14.6),
    m = oo,
    tag = "param_tfhe_630_gaussian_classic_128_32"
)

param_tfhe_1024_binary_classic_128_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**8.3),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_128_32"
)

param_tfhe_1024_ternary_classic_128_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**7.1),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_128_32"
)

param_tfhe_1024_gaussian_classic_128_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**4.6),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_128_32"
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


# q = 2**64

param_tfhe_630_binary_classic_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**50.5),
    m = oo,
    tag = "param_tfhe_630_binary_classic_128"
)

param_tfhe_630_ternary_classic_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**49.2),
    m = oo,
    tag = "param_tfhe_630_ternary_classic_128"
)

param_tfhe_630_gaussian_classic_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**46.6),
    m = oo,
    tag = "param_tfhe_630_gaussian_classic_128"
)

param_tfhe_750_binary_classic_128 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**47.4),
    m = oo,
    tag = "param_tfhe_750_binary_classic_128"
)

param_tfhe_750_ternary_classic_128 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**46.2),
    m = oo,
    tag = "param_tfhe_750_ternary_classic_128"
)

param_tfhe_750_gaussian_classic_128 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**43.5),
    m = oo,
    tag = "param_tfhe_750_gaussian_classic_128"
)

param_tfhe_870_binary_classic_128 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**44.3),
    m = oo,
    tag = "param_tfhe_870_binary_classic_128"
)

param_tfhe_870_ternary_classic_128 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**43.1),
    m = oo,
    tag = "param_tfhe_870_ternary_classic_128"
)

param_tfhe_870_gaussian_classic_128 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**40.3),
    m = oo,
    tag = "param_tfhe_870_gaussian_classic_128"
)

param_tfhe_1024_binary_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**40.3),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_128"
)

param_tfhe_1024_ternary_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**39.1),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_128"
)

param_tfhe_1024_gaussian_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**36.4),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_128"
)

param_tfhe_2048_binary_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**13.7),
    m = oo,
    tag = "param_tfhe_2048_binary_classic_128"
)

param_tfhe_2048_ternary_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**12.4),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_128"
)

param_tfhe_2048_gaussian_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**10.0),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_128"
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

Table_5_3_a = [
             (param_tfhe_630_binary_classic_128_32, 128, classic_model),
             (param_tfhe_630_ternary_classic_128_32, 128, classic_model),
             (param_tfhe_630_gaussian_classic_128_32, 128, classic_model), 
             (param_tfhe_1024_binary_classic_128_32, 128, classic_model),
             (param_tfhe_1024_ternary_classic_128_32, 128, classic_model),
             (param_tfhe_1024_gaussian_classic_128_32, 128, classic_model),
             (param_tfhe_2048_binary_classic_128_32, 128, classic_model),
             (param_tfhe_2048_ternary_classic_128_32, 128, classic_model),
             (param_tfhe_2048_gaussian_classic_128_32, 128, classic_model),      
             (param_tfhe_630_binary_classic_128, 128, classic_model),
             (param_tfhe_630_ternary_classic_128, 128, classic_model),
             (param_tfhe_630_gaussian_classic_128, 128, classic_model),
             (param_tfhe_750_binary_classic_128, 128, classic_model),
             (param_tfhe_750_ternary_classic_128, 128, classic_model),
             (param_tfhe_750_gaussian_classic_128, 128, classic_model),
             (param_tfhe_870_binary_classic_128, 128, classic_model),
             (param_tfhe_870_ternary_classic_128, 128, classic_model),
             (param_tfhe_870_gaussian_classic_128, 128, classic_model),
             (param_tfhe_1024_binary_classic_128, 128, classic_model),
             (param_tfhe_1024_ternary_classic_128, 128, classic_model),
             (param_tfhe_1024_gaussian_classic_128, 128, classic_model),
             (param_tfhe_2048_binary_classic_128, 128, classic_model),
             (param_tfhe_2048_ternary_classic_128, 128, classic_model),
             (param_tfhe_2048_gaussian_classic_128, 128, classic_model),
             (param_tfhe_4096_binary_classic_128, 128, classic_model),
             (param_tfhe_4096_ternary_classic_128, 128, classic_model),
             (param_tfhe_4096_gaussian_classic_128, 128, classic_model)]


# q = 2**32

param_tfhe_630_binary_classic_192_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**22.1),
    m = oo,
    tag = "param_tfhe_630_binary_classic_192_32"
)

param_tfhe_630_ternary_classic_192_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**20.8),
    m = oo,
    tag = "param_tfhe_630_ternary_classic_192_32"
)

param_tfhe_630_gaussian_classic_192_32 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**17.9),
    m = oo,
    tag = "param_tfhe_630_gaussian_classic_192_32"
)

param_tfhe_1024_binary_classic_192_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**17.2),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_192_32"
)

param_tfhe_1024_ternary_classic_192_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**15.9),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_192_32"
)

param_tfhe_1024_gaussian_classic_192_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**13.0),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_192_32"
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

# q = 2**64

param_tfhe_750_binary_classic_192 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**52.0),
    m = oo,
    tag = "param_tfhe_750_binary_classic_192"
)

param_tfhe_750_ternary_classic_192 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**50.6),
    m = oo,
    tag = "param_tfhe_750_ternary_classic_192"
)

param_tfhe_750_gaussian_classic_192 = LWE.Parameters(
    n = 750,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**47.7),
    m = oo,
    tag = "param_tfhe_750_gaussian_classic_192"
)

param_tfhe_870_binary_classic_192 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**52.0),
    m = oo,
    tag = "param_tfhe_870_binary_classic_192"
)

param_tfhe_870_ternary_classic_192 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**50.6),
    m = oo,
    tag = "param_tfhe_870_ternary_classic_192"
)

param_tfhe_870_gaussian_classic_192 = LWE.Parameters(
    n = 870,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**47.7),
    m = oo,
    tag = "param_tfhe_870_gaussian_classic_192"
)

param_tfhe_1024_binary_classic_192 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**49.2),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_192"
)

param_tfhe_1024_ternary_classic_192 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**47.9),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_192"
)

param_tfhe_1024_gaussian_classic_192 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**45.0),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_192"
)

param_tfhe_2048_binary_classic_192 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**30.9),
    m = oo,
    tag = "param_tfhe_2048_binary_classic_192"
)

param_tfhe_2048_ternary_classic_192 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**29.5),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_192"
)

param_tfhe_2048_gaussian_classic_192 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**26.5),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_192"
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

Table_5_3_b = [
             (param_tfhe_1024_binary_classic_192_32, 192, classic_model),
             (param_tfhe_1024_ternary_classic_192_32, 192, classic_model),
             (param_tfhe_1024_gaussian_classic_192_32, 192, classic_model),
             (param_tfhe_2048_binary_classic_192_32, 192, classic_model),
             (param_tfhe_2048_ternary_classic_192_32, 192, classic_model),
             (param_tfhe_2048_gaussian_classic_192_32, 192, classic_model),
             (param_tfhe_630_binary_classic_192, 192, classic_model),
             (param_tfhe_630_ternary_classic_192, 192, classic_model),
             (param_tfhe_630_gaussian_classic_192, 192, classic_model),
             (param_tfhe_750_binary_classic_192, 192, classic_model),
             (param_tfhe_750_ternary_classic_192, 192, classic_model),
             (param_tfhe_750_gaussian_classic_192, 192, classic_model),
             (param_tfhe_870_binary_classic_192, 192, classic_model),
             (param_tfhe_870_ternary_classic_192, 192, classic_model),
             (param_tfhe_870_gaussian_classic_192, 192, classic_model),
             (param_tfhe_1024_binary_classic_192, 192, classic_model),
             (param_tfhe_1024_ternary_classic_192, 192, classic_model),
             (param_tfhe_1024_gaussian_classic_192, 192, classic_model),
             (param_tfhe_2048_binary_classic_192, 192, classic_model),
             (param_tfhe_2048_ternary_classic_192, 192, classic_model),
             (param_tfhe_2048_gaussian_classic_192, 192, classic_model),
             (param_tfhe_4096_binary_classic_192, 192, classic_model),
             (param_tfhe_4096_ternary_classic_192, 192, classic_model),
             (param_tfhe_4096_gaussian_classic_192, 192, classic_model)]
# q = 2**32

param_tfhe_1024_binary_classic_256_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**21.8),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_256_32"
)

param_tfhe_1024_ternary_classic_256_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**20.5),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_256_32"
)

param_tfhe_1024_gaussian_classic_256_32 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**17.4),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_256_32"
)

param_tfhe_2048_binary_classic_256_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**7.6),
    m = oo,
    tag = "param_tfhe_2048_binary_classic_256_32"
)

param_tfhe_2048_ternary_classic_256_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**6.1),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_256_32"
)

param_tfhe_2048_gaussian_classic_256_32 = LWE.Parameters(
    n = 2048,
    q = 2**32,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**3.2),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_256_32"
)


# q = 2**64

param_tfhe_1024_binary_classic_256 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**53.8),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_256"
)

param_tfhe_1024_ternary_classic_256 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**52.5),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_256"
)

param_tfhe_1024_gaussian_classic_256 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**49.4),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_256"
)

param_tfhe_2048_binary_classic_256 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2*39.6),
    m = oo,
    tag = "param_tfhe_2048_binary_classic_256"
)

param_tfhe_2048_ternary_classic_256 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**38.1),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_256"
)

param_tfhe_2048_gaussian_classic_256 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**35.0),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_256"
)

param_tfhe_4096_binary_classic_256 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**10.9),
    m = oo,
    tag = "param_tfhe_4096_binary_classic_256"
)

param_tfhe_4096_ternary_classic_256 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**9.3),
    m = oo,
    tag = "param_tfhe_4096_ternary_classic_256"
)

param_tfhe_4096_gaussian_classic_256 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**6.4),
    m = oo,
    tag = "param_tfhe_4096_gaussian_classic_256"
)

param_tfhe_8192_binary_classic_256 = LWE.Parameters(
    n = 8192,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2),
    m = oo,
    tag = "param_tfhe_8192_binary_quantum_256"
)


Table_5_3_c = [
            (param_tfhe_1024_binary_classic_256_32, 256, classic_model),
             (param_tfhe_1024_ternary_classic_256_32, 256, classic_model),
             (param_tfhe_1024_gaussian_classic_256_32, 256, classic_model),
             (param_tfhe_2048_binary_classic_256_32, 256, classic_model),
             (param_tfhe_2048_ternary_classic_256_32, 256, classic_model),
             (param_tfhe_2048_gaussian_classic_256_32, 256, classic_model),
             (param_tfhe_1024_binary_classic_256, 256, classic_model),
             (param_tfhe_1024_ternary_classic_256, 256, classic_model),
             (param_tfhe_1024_gaussian_classic_256, 256, classic_model),
             (param_tfhe_2048_binary_classic_256, 256, classic_model),
             (param_tfhe_2048_ternary_classic_256, 256, classic_model),
             (param_tfhe_2048_gaussian_classic_256, 256, classic_model),
             (param_tfhe_4096_binary_classic_256, 256, classic_model),
             (param_tfhe_4096_ternary_classic_256, 256, classic_model),
             (param_tfhe_4096_gaussian_classic_256, 256, classic_model),
             (param_tfhe_8192_binary_classic_256, 256, classic_model)]

Tables = [Table_5_2_a,
          Table_5_2_b,
          Table_5_2_c,
          Table_5_2_d,
          Table_5_2_e,
          Table_5_2_f,
          Table_5_3_a,
          Table_5_3_b,
          Table_5_3_c]

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
