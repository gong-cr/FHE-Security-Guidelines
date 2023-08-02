import sys
sys.path.insert(1, '../lattice-estimator')
from estimator import *

classic_model = RC.BDGL16
quantum_model = RC.LaaMosPol14

# Table 4.1

param_8192_ternary_classic_128 = LWE.Parameters(
    n = 8192,
    q = 2**214,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_classic_128"
)

param_8192_ternary_quantum_128 = LWE.Parameters(
    n = 8192,
    q = 2**204,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_8192_ternary_quantum_128"
)

param_16384_ternary_classic_128 = LWE.Parameters(
    n = 16384,
    q = 2**431,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_classic_128"
)

#TODO: update param_16384_ternary_quantum_128 (121-bits)
param_16384_ternary_quantum_128 = LWE.Parameters(
    n = 16384,
    q = 2**410,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_quantum_128"
)

param_32768_ternary_classic_128 = LWE.Parameters(
    n = 32768,
    q = 2**867,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_classic_128"
)

param_32768_ternary_quantum_128 = LWE.Parameters(
    n = 32768,
    q = 2**823,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_quantum_128"
)

param_65536_ternary_classic_128 = LWE.Parameters(
    n = 65536,
    q = 2**1745,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_classic_128"
)

param_65536_ternary_quantum_128 = LWE.Parameters(
    n = 65536,
    q = 2**1656,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_quantum_128"
)

param_131072_ternary_classic_128 = LWE.Parameters(
    n = 131072,
    q = 2**3515,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_classic_128"
)

param_131072_ternary_quantum_128 = LWE.Parameters(
    n = 131072,
    q = 2**3337,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_quantum_128"
)

Table_4_1 = [(param_8192_ternary_classic_128, 128, classic_model),
             (param_8192_ternary_quantum_128, 128, quantum_model),
             (param_16384_ternary_classic_128, 128, classic_model),
             (param_16384_ternary_quantum_128, 128, quantum_model),
             (param_32768_ternary_classic_128, 128, classic_model),
             (param_32768_ternary_quantum_128, 128, quantum_model),
             (param_65536_ternary_classic_128, 128, classic_model),
             (param_65536_ternary_quantum_128, 128, quantum_model),
             (param_131072_ternary_classic_128, 128, classic_model),
             (param_131072_ternary_quantum_128, 128, quantum_model)] 

# Table 4.2

param_8192_ternary_classic_192 = LWE.Parameters(
    n = 8192,
    q = 2**148,
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
    q = 2**297,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_classic_192"
)

param_16384_ternary_quantum_192 = LWE.Parameters(
    n = 16384,
    q = 2**283,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary_quantum_192"
)

param_32768_ternary_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**596,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_classic_192"
)

param_32768_ternary_quantum_192 = LWE.Parameters(
    n = 32768,
    q = 2**570,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary_quantum_192"
)

param_65536_ternary_classic_192 = LWE.Parameters(
    n = 65536,
    q = 2**1196,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_classic_192"
)

param_65536_ternary_quantum_192 = LWE.Parameters(
    n = 65536,
    q = 2**1143,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_quantum_192"
)

param_131072_ternary_classic_192 = LWE.Parameters(
    n = 131072,
    q = 2**2400,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_classic_192"
)

param_131072_ternary_quantum_192 = LWE.Parameters(
    n = 131072,
    q = 2**2296,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_quantum_192"
)

Table_4_2 = [(param_8192_ternary_classic_192, 192, classic_model),
             (param_8192_ternary_quantum_192, 192, quantum_model),
             (param_16384_ternary_classic_192, 192, classic_model),
             (param_16384_ternary_quantum_192, 192, quantum_model),
             (param_32768_ternary_classic_192, 192, classic_model),
             (param_32768_ternary_quantum_192, 192, quantum_model),
             (param_65536_ternary_classic_192, 192, classic_model),
             (param_65536_ternary_quantum_192, 192, quantum_model),
             (param_131072_ternary_classic_192, 192, classic_model),
             (param_131072_ternary_quantum_192, 192, quantum_model)]

# Table 4.3

param_8192_ternary_classic_256 = LWE.Parameters(
    n = 8192,
    q = 2**114,
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
    q = 2**230,
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
    q = 2**462,
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
    q = 2**927,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_classic_256"
)

param_65536_ternary_quantum_256 = LWE.Parameters(
    n = 65536,
    q = 2**887,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary_quantum_256"
)

param_131072_ternary_classic_256 = LWE.Parameters(
    n = 131072,
    q = 2**1865,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_classic_256"
)

param_131072_ternary_quantum_256 = LWE.Parameters(
    n = 131072,
    q = 2**1781,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary_quantum_256"
)

Table_4_3 = [(param_8192_ternary_classic_256, 256, classic_model),
             (param_8192_ternary_quantum_256, 256, quantum_model),
             (param_16384_ternary_classic_256, 256, classic_model),
             (param_16384_ternary_quantum_256, 256, quantum_model),
             (param_32768_ternary_classic_256, 256, classic_model),
             (param_32768_ternary_quantum_256, 256, quantum_model),
             (param_65536_ternary_classic_256, 256, classic_model),
             (param_65536_ternary_quantum_256, 256, quantum_model),
             (param_131072_ternary_classic_256, 256, classic_model),
             (param_131072_ternary_quantum_256, 256, quantum_model)]

# Table 4.4

param_16384_ternary128_classic_128 = LWE.Parameters(
    n = 16384,
    q = 2**361,
    Xs = ND.SparseTernary(16384, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary128_classic_128"
)

param_16384_ternary128_quantum_128 = LWE.Parameters(
    n = 16384,
    q = 2**342,
    Xs = ND.SparseTernary(16384, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary128_quantum_128"
)

param_16384_ternary256_classic_128 = LWE.Parameters(
    n = 16384,
    q = 2**413,
    Xs = ND.SparseTernary(16384, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary256_classic_128"
)

param_16384_ternary256_quantum_128 = LWE.Parameters(
    n = 16384,
    q = 2**387,
    Xs = ND.SparseTernary(16384, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary256_quantum_128"
)

param_32768_ternary128_classic_128 = LWE.Parameters(
    n = 32768,
    q = 2**718,
    Xs = ND.SparseTernary(32768, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary128_classic_128"
)

param_32768_ternary128_quantum_128 = LWE.Parameters(
    n = 32768,
    q = 2**675,
    Xs = ND.SparseTernary(32768, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary128_quantum_128"
)

param_32768_ternary256_classic_128 = LWE.Parameters(
    n = 32768,
    q = 2**818,
    Xs = ND.SparseTernary(32768, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary256_classic_128"
)

param_32768_ternary256_quantum_128 = LWE.Parameters(
    n = 32768,
    q = 2**768,
    Xs = ND.SparseTernary(32768, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary256_quantum_128"
)

param_65536_ternary128_classic_128 = LWE.Parameters(
    n = 65536,
    q = 2**1450,
    Xs = ND.SparseTernary(65536, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary128_classic_128"
)

param_65536_ternary128_quantum_128 = LWE.Parameters(
    n = 65536,
    q = 2**1359,
    Xs = ND.SparseTernary(65536, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary128_quantum_128"
)

param_65536_ternary256_classic_128 = LWE.Parameters(
    n = 65536,
    q = 2**1637,
    Xs = ND.SparseTernary(65536, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary256_classic_128"
)

param_65536_ternary256_quantum_128 = LWE.Parameters(
    n = 65536,
    q = 2**1537,
    Xs = ND.SparseTernary(65536, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary256_quantum_128"
)

param_131072_ternary128_classic_128 = LWE.Parameters(
    n = 131072,
    q = 2**2950,
    Xs = ND.SparseTernary(131072, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary128_classic_128"
)

param_131072_ternary128_quantum_128 = LWE.Parameters(
    n = 131072,
    q = 2**2775,
    Xs = ND.SparseTernary(131072, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary128_quantum_128"
)

param_131072_ternary256_classic_128 = LWE.Parameters(
    n = 131072,
    q = 2**3325,
    Xs = ND.SparseTernary(131072, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary256_classic_128"
)

param_131072_ternary256_quantum_128 = LWE.Parameters(
    n = 131072,
    q = 2**3112,
    Xs = ND.SparseTernary(131072, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary256_quantum_128"
)

Table_4_4 = [(param_16384_ternary128_classic_128, 128, classic_model),
             (param_16384_ternary128_quantum_128, 128, quantum_model),
             (param_16384_ternary256_classic_128, 128, classic_model),
             (param_16384_ternary256_quantum_128, 128, quantum_model),
             (param_32768_ternary128_classic_128, 128, classic_model),
             (param_32768_ternary128_quantum_128, 128, quantum_model),
             (param_32768_ternary256_classic_128, 128, classic_model),
             (param_32768_ternary256_quantum_128, 128, quantum_model),
             (param_65536_ternary128_classic_128, 128, classic_model),
             (param_65536_ternary128_quantum_128, 128, quantum_model),
             (param_65536_ternary256_classic_128, 128, classic_model),
             (param_65536_ternary256_quantum_128, 128, quantum_model),
             (param_131072_ternary128_classic_128, 128, classic_model),
             (param_131072_ternary128_quantum_128, 128, quantum_model),
             (param_131072_ternary256_classic_128, 128, classic_model),
             (param_131072_ternary256_quantum_128, 128, quantum_model)]

# Table 4.5

param_16384_ternary128_classic_192 = LWE.Parameters(
    n = 16384,
    q = 2**202,
    Xs = ND.SparseTernary(16384, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary128_classic_192"
)

param_16384_ternary128_quantum_192 = LWE.Parameters(
    n = 16384,
    q = 2**190,
    Xs = ND.SparseTernary(16384, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary128_quantum_192"
)

param_16384_ternary256_classic_192 = LWE.Parameters(
    n = 16384,
    q = 2**270,
    Xs = ND.SparseTernary(16384, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary256_classic_192"
)

param_16384_ternary256_quantum_192 = LWE.Parameters(
    n = 16384,
    q = 2**253,
    Xs = ND.SparseTernary(16384, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary256_quantum_192"
)

param_32768_ternary128_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**404,
    Xs = ND.SparseTernary(32768, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary128_classic_192"
)

param_32768_ternary128_quantum_192 = LWE.Parameters(
    n = 32768,
    q = 2**377,
    Xs = ND.SparseTernary(32768, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary128_quantum_192"
)

param_32768_ternary256_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**531,
    Xs = ND.SparseTernary(32768, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary256_classic_192"
)

param_32768_ternary256_quantum_192 = LWE.Parameters(
    n = 32768,
    q = 2**499,
    Xs = ND.SparseTernary(32768, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary256_quantum_192"
)

param_65536_ternary128_classic_192 = LWE.Parameters(
    n = 65536,
    q = 2**821,
    Xs = ND.SparseTernary(65536, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary128_classic_192"
)

param_65536_ternary128_quantum_192 = LWE.Parameters(
    n = 65536,
    q = 2**768,
    Xs = ND.SparseTernary(65536, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary128_quantum_192"
)

param_65536_ternary256_classic_192 = LWE.Parameters(
    n = 65536,
    q = 2**1068,
    Xs = ND.SparseTernary(65536, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary256_classic_192"
)

param_65536_ternary256_quantum_192 = LWE.Parameters(
    n = 65536,
    q = 2**1002,
    Xs = ND.SparseTernary(65536, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary256_quantum_192"
)

param_131072_ternary128_classic_192 = LWE.Parameters(
    n = 131072,
    q = 2**1700,
    Xs = ND.SparseTernary(131072, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary128_classic_192"
)

param_131072_ternary128_quantum_192 = LWE.Parameters(
    n = 131072,
    q = 2**1575,
    Xs = ND.SparseTernary(131072, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary128_quantum_192"
)

param_131072_ternary256_classic_192 = LWE.Parameters(
    n = 131072,
    q = 2**2187,
    Xs = ND.SparseTernary(131072, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary256_classic_192"
)

param_131072_ternary256_quantum_192 = LWE.Parameters(
    n = 131072,
    q = 2**2043,
    Xs = ND.SparseTernary(131072, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary256_quantum_192"
)

Table_4_5 = [(param_16384_ternary128_classic_192, 192, classic_model),
             (param_16384_ternary128_quantum_192, 192, quantum_model),
             (param_16384_ternary256_classic_192, 192, classic_model),
             (param_16384_ternary256_quantum_192, 192, quantum_model),
             (param_32768_ternary128_classic_192, 192, classic_model),
             (param_32768_ternary128_quantum_192, 192, quantum_model),
             (param_32768_ternary256_classic_192, 192, classic_model),
             (param_32768_ternary256_quantum_192, 192, quantum_model),
             (param_65536_ternary128_classic_192, 192, classic_model),
             (param_65536_ternary128_quantum_192, 192, quantum_model),
             (param_65536_ternary256_classic_192, 192, classic_model),
             (param_65536_ternary256_quantum_192, 192, quantum_model),
             (param_131072_ternary128_classic_192, 192, classic_model),
             (param_131072_ternary128_quantum_192, 192, quantum_model),
             (param_131072_ternary256_classic_192, 192, classic_model),
             (param_131072_ternary256_quantum_192, 192, quantum_model)]

# Table 4.6

param_16384_ternary128_classic_256 = LWE.Parameters(
    n = 16384,
    q = 2**125,
    Xs = ND.SparseTernary(16384, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary128_classic_256"
)

param_16384_ternary128_quantum_256 = LWE.Parameters(
    n = 16384,
    q = 2**118,
    Xs = ND.SparseTernary(16384, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary128_quantum_256"
)

param_16384_ternary256_classic_256 = LWE.Parameters(
    n = 16384,
    q = 2**194,
    Xs = ND.SparseTernary(16384, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary256_classic_256"
)

param_16384_ternary256_quantum_256 = LWE.Parameters(
    n = 16384,
    q = 2**182,
    Xs = ND.SparseTernary(16384, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_16384_ternary256_quantum_256"
)

param_32768_ternary128_classic_256 = LWE.Parameters(
    n = 32768,
    q = 2**245,
    Xs = ND.SparseTernary(32768, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary128_classic_256"
)

param_32768_ternary128_quantum_256 = LWE.Parameters(
    n = 32768,
    q = 2**230,
    Xs = ND.SparseTernary(32768, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary128_quantum_256"
)

param_32768_ternary256_classic_256 = LWE.Parameters(
    n = 32768,
    q = 2**378,
    Xs = ND.SparseTernary(32768, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary256_classic_256"
)

param_32768_ternary256_quantum_256 = LWE.Parameters(
    n = 32768,
    q = 2**354,
    Xs = ND.SparseTernary(32768, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_32768_ternary256_quantum_256"
)

param_65536_ternary128_classic_256 = LWE.Parameters(
    n = 65536,
    q = 2**493,
    Xs = ND.SparseTernary(65536, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary128_classic_256"
)

param_65536_ternary128_quantum_256 = LWE.Parameters(
    n = 65536,
    q = 2**461,
    Xs = ND.SparseTernary(65536, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary128_quantum_256"
)

param_65536_ternary256_classic_256 = LWE.Parameters(
    n = 65536,
    q = 2**772,
    Xs = ND.SparseTernary(65536, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary256_classic_256"
)

param_65536_ternary256_quantum_256 = LWE.Parameters(
    n = 65536,
    q = 2**721,
    Xs = ND.SparseTernary(65536, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_65536_ternary256_quantum_256"
)

param_131072_ternary128_classic_256 = LWE.Parameters(
    n = 131072,
    q = 2**1018,
    Xs = ND.SparseTernary(131072, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary128_classic_256"
)

param_131072_ternary128_quantum_256 = LWE.Parameters(
    n = 131072,
    q = 2**951,
    Xs = ND.SparseTernary(131072, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary128_quantum_256"
)

param_131072_ternary256_classic_256 = LWE.Parameters(
    n = 131072,
    q = 2**1531,
    Xs = ND.SparseTernary(131072, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary256_classic_256"
)

param_131072_ternary256_quantum_256 = LWE.Parameters(
    n = 131072,
    q = 2**1425,
    Xs = ND.SparseTernary(131072, 128, 128),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_131072_ternary256_quantum_256"
)

Table_4_6 = [(param_16384_ternary128_classic_256, 256, classic_model),
             (param_16384_ternary128_quantum_256, 256, quantum_model),
             (param_16384_ternary256_classic_256, 256, classic_model),
             (param_16384_ternary256_quantum_256, 256, classic_model),
             (param_32768_ternary128_classic_256, 256, quantum_model),
             (param_32768_ternary128_quantum_256, 256, classic_model),
             (param_32768_ternary256_classic_256, 256, quantum_model),
             (param_32768_ternary256_quantum_256, 256, classic_model),
             (param_65536_ternary128_classic_256, 256, quantum_model),
             (param_65536_ternary128_quantum_256, 256, classic_model),
             (param_65536_ternary256_classic_256, 256, quantum_model),
             (param_65536_ternary256_quantum_256, 256, classic_model),
             (param_131072_ternary128_classic_256, 256, quantum_model),
             (param_131072_ternary128_quantum_256, 256, classic_model),
             (param_131072_ternary256_classic_256, 256, quantum_model),
             (param_131072_ternary256_quantum_256, 256, classic_model)]

# Table 4.7 (we ignore q = 2**32 as the relative error is the same)

param_tfhe_630_binary_classic_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**49.9),
    m = oo,
    tag = "param_tfhe_630_binary_classic_128"
)

param_tfhe_630_binary_quantum_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**50.9),
    m = oo,
    tag = "param_tfhe_630_binary_quantum_128"
)

param_tfhe_630_ternary_classic_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**48.6),
    m = oo,
    tag = "param_tfhe_630_ternary_classic_128"
)

param_tfhe_630_ternary_quantum_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(2**49.7),
    m = oo,
    tag = "param_tfhe_630_ternary_quantum_128"
)

#TODO: update
param_tfhe_630_gaussian_classic_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**46.2),
    m = oo,
    tag = "param_tfhe_630_gaussian_classic_128"
)

#TODO: update
param_tfhe_630_gaussian_quantum_128 = LWE.Parameters(
    n = 630,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**47.3),
    m = oo,
    tag = "param_tfhe_630_gaussian_quantum_128"
)

#TODO: update
param_tfhe_1024_binary_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**39.5),
    m = oo,
    tag = "param_tfhe_1024_binary_classic_128"
)

param_tfhe_1024_binary_quantum_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**41.2),
    m = oo,
    tag = "param_tfhe_1024_binary_quantum_128"
)

#TODO: update
param_tfhe_1024_ternary_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**38.3),
    m = oo,
    tag = "param_tfhe_1024_ternary_classic_128"
)

param_tfhe_1024_ternary_quantum_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**40.0),
    m = oo,
    tag = "param_tfhe_1024_ternary_quantum_128"
)

param_tfhe_1024_gaussian_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**36.1),
    m = oo,
    tag = "param_tfhe_1024_gaussian_classic_128"
)

#TODO: update
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

param_tfhe_2048_binary_quantum_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**16.0),
    m = oo,
    tag = "param_tfhe_2048_binary_quantum_128"
)

#TODO: update
param_tfhe_2048_ternary_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**11.4),
    m = oo,
    tag = "param_tfhe_2048_ternary_classic_128"
)

#TODO: update
param_tfhe_2048_ternary_quantum_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**14.8),
    m = oo,
    tag = "param_tfhe_2048_ternary_quantum_128"
)

param_tfhe_2048_gaussian_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**9.4),
    m = oo,
    tag = "param_tfhe_2048_gaussian_classic_128"
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

param_tfhe_4096_binary_quantum_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_binary_quantum_128"
)

param_tfhe_4096_ternary_classic_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_ternary_classic_128"
)

param_tfhe_4096_ternary_quantum_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_ternary_quantum_128"
)

param_tfhe_4096_gaussian_classic_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_gaussian_classic_128"
)

param_tfhe_4096_gaussian_quantum_128 = LWE.Parameters(
    n = 4096,
    q = 2**64,
    Xs = ND.DiscreteGaussian(4),
    Xe = ND.DiscreteGaussian(2**2.0),
    m = oo,
    tag = "param_tfhe_4096_gaussian_quantum_128"
)

Table_4_7 = [(param_tfhe_630_binary_classic_128, 128, classic_model),
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

# Table 4.9

param_functional_16384_classic_128 = LWE.Parameters(
    n = 16384,
    q = 2**424,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_16384_classic_128"
)

param_functional_16384_quantum_128 = LWE.Parameters(
    n = 16384,
    q = 2**391,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_16384_quantum_128"
)

param_functional_16384_classic_192 = LWE.Parameters(
    n = 16384,
    q = 2**285,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_16384_classic_192"
)

param_functional_16384_quantum_192 = LWE.Parameters(
    n = 16384,
    q = 2**285,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_16384_quantum_192"
)

param_functional_16384_classic_256 = LWE.Parameters(
    n = 16384,
    q = 2**225,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_16384_classic_256"
)

param_functional_16384_quantum_256 = LWE.Parameters(
    n = 16384,
    q = 2**215,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_16384_quantum_256"
)

param_functional_32768_classic_128 = LWE.Parameters(
    n = 32768,
    q = 2**855,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_32768_classic_128"
)

param_functional_32768_quantum_128 = LWE.Parameters(
    n = 32768,
    q = 2**815,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_32768_quantum_128"
)

param_functional_32768_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**585,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_32768_classic_192"
)

param_functional_32768_quantum_192 = LWE.Parameters(
    n = 32768,
    q = 2**572,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_32768_quantum_192"
)

param_functional_32768_classic_256 = LWE.Parameters(
    n = 32768,
    q = 2**455,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_32768_classic_256"
)

param_functional_32768_quantum_256 = LWE.Parameters(
    n = 32768,
    q = 2**435,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_32768_quantum_256"
)

param_functional_65536_classic_128 = LWE.Parameters(
    n = 65536,
    q = 2**1730,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_classic_128"
)

param_functional_65536_quantum_128 = LWE.Parameters(
    n = 65536,
    q = 2**1640,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_quantum_128"
)

param_functional_65536_classic_192 = LWE.Parameters(
    n = 65536,
    q = 2**1180,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_classic_192"
)

param_functional_65536_quantum_192 = LWE.Parameters(
    n = 65536,
    q = 2**1120,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_quantum_192"
)

param_functional_65536_classic_256 = LWE.Parameters(
    n = 65536,
    q = 2**930,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_classic_256"
)

param_functional_65536_quantum_256 = LWE.Parameters(
    n = 65536,
    q = 2**880,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_quantum_256"
)


Table_4_8 = [
    (param_functional_16384_classic_128, 128, classic_model),
    (param_functional_16384_quantum_128, 128, quantum_model),
    (param_functional_16384_classic_192, 192, classic_model),
    (param_functional_16384_quantum_192, 192, quantum_model),
    (param_functional_16384_classic_256, 256, classic_model),
    (param_functional_16384_quantum_256, 256, quantum_model),
    (param_functional_32768_classic_128, 128, classic_model),
    (param_functional_32768_quantum_128, 128, quantum_model),
    (param_functional_32768_classic_192, 192, classic_model),
    (param_functional_32768_quantum_192, 192, quantum_model),
    (param_functional_32768_classic_256, 256, classic_model),
    (param_functional_32768_quantum_256, 256, quantum_model),
    (param_functional_65536_classic_128, 128, classic_model),
    (param_functional_65536_quantum_128, 128, quantum_model),
    (param_functional_65536_classic_192, 192, classic_model),
    (param_functional_65536_quantum_192, 192, quantum_model),
    (param_functional_65536_classic_256, 256, classic_model),
    (param_functional_65536_quantum_256, 256, quantum_model)
]

# Table 4.9

param_functional_tfhe_742_binary_classic_128 = LWE.Parameters(
    n = 742,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**(-17.11) * 2**64),
    m = oo,
    tag = "param_functional_tfhe_742_binary_classic_128"
)

param_functional_tfhe_2048_binary_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**(-51.6) * 2**64),
    m = oo,
    tag = "param_functional_tfhe_2048_binary_classic_128"
)

param_functional_tfhe_777_binary_classic_128 = LWE.Parameters(
    n = 777,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**(-18.03) * 2**64),
    m = oo,
    tag = "param_functional_tfhe_777_binary_classic_128"
)

param_functional_tfhe_1536_binary_classic_128 = LWE.Parameters(
    n = 512 * 3,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**(-38.08) * 2**64),
    m = oo,
    tag = "param_functional_tfhe_1536_binary_classic_128"
)

Table_4_9 = [
    (param_functional_tfhe_742_binary_classic_128, 128, classic_model),
    (param_functional_tfhe_2048_binary_classic_128, 128, classic_model),
    (param_functional_tfhe_777_binary_classic_128, 128, classic_model),
    (param_functional_tfhe_1536_binary_classic_128, 128, classic_model)
]

#Table 4.10

param_functional_131072_ternary128_classic_128 = LWE.Parameters(
    n = 131072,
    q = 2**2292,
    Xs = ND.SparseTernary(131072, 64, 64),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_131072_ternary128_classic_128"
)

param_functional_131072_ternary64_classic_128 = LWE.Parameters(
    n = 131072,
    q = 2**1937,
    Xs = ND.SparseTernary(131072, 32, 32),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_131072_ternary64_classic_128"
)

Table_4_10 = [
    (param_functional_131072_ternary128_classic_128, 128, classic_model),
    (param_functional_131072_ternary64_classic_128, 128, quantum_model)
]

# Table 4.11

param_functional_32768_ternary21845_classic_128 = LWE.Parameters(
    n = 32768,
    q = 2**866,
    Xs = ND.SparseTernary(32768, 10922, 10923),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_32768_ternary21845_classic_128"
)

param_functional_65536_ternary8192_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**899,
    Xs = ND.SparseTernary(65536, 4096, 4096),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_ternary8192_classic_192"
)

param_functional_65536_ternary8192_classic_256 = LWE.Parameters(
    n = 32768,
    q = 2**674,
    Xs = ND.SparseTernary(65536, 4096, 4096),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_ternary21845_classic_256"
)

param_functional_32768_ternary21845_quantum_128 = LWE.Parameters(
    n = 32768,
    q = 2**571,
    Xs = ND.SparseTernary(32768, 10922, 10923),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_32768_ternary21845_quantum_128"
)

param_functional_65536_ternary8192_quantum_192 = LWE.Parameters(
    n = 32768,
    q = 2**862,
    Xs = ND.SparseTernary(65536, 4096, 4096),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_ternary8192_quantum_192"
)

param_functional_65536_ternary8192_quantum_256 = LWE.Parameters(
    n = 32768,
    q = 2**622,
    Xs = ND.SparseTernary(65536, 4096, 4096),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_ternary21845_quantum_256"
)

Table_4_11 = [
    (param_functional_32768_ternary21845_classic_128, 128, classic_model),
    (param_functional_65536_ternary8192_classic_192, 192, classic_model),
    (param_functional_65536_ternary8192_classic_256, 256, classic_model),
    (param_functional_32768_ternary21845_quantum_128, 128, quantum_model),
    (param_functional_65536_ternary8192_quantum_192, 192, quantum_model),
    (param_functional_65536_ternary8192_quantum_256, 256, quantum_model)
]

all_security_params = Table_4_1 + Table_4_2 + Table_4_3 + Table_4_4 + Table_4_5 + Table_4_6 + Table_4_7
all_functional_params = Table_4_8 + Table_4_9 + Table_4_10 + Table_4_11
all_params = all_security_params + all_functional_params



for (param, security_level, model) in all_params:
    print("parameters = {}".format(param.tag))
    params_to_update = []
    try:
        usvp_level = LWE.primal_usvp(param, red_cost_model = model)
        dual_level = LWE.dual_hybrid(param, red_cost_model = model)
        estimator_level = log(min(usvp_level["rop"], dual_level["rop"]),2)
        if security_level > estimator_level:
            print("target security level = {}".format(security_level))
            print("attained security level = {}".format(estimator_level))
            params_to_update.append(param)
        else:
            print("pass.")
    except Exception as e:
        print(e)
        print("fail.")

print(params_to_update)