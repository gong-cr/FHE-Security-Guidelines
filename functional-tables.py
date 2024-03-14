import sys
sys.path.insert(1, 'lattice-estimator')
from estimator import *

classic_model = RC.BDGL16

# Table 5.4 BFV / BGV without bootstrapping

bfvbgv_nobootstrap_16384_classic_128 = LWE.Parameters(
    n = 16384,
    q = 2**424,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "bfvbgv_nobootstrap_16384_classic"
)

bfvbgv_nobootstrap_16384_quantum_128 = LWE.Parameters(
    n = 16384,
    q = 2**391,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "bfvbgv_nobootstrap_16384_quantum_128"
)

bfvbgv_nobootstrap_32768_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**585,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "bfvbgv_nobootstrap_32768_classic_192"
)

bfvbgv_nobootstrap_32768_quantum_192 = LWE.Parameters(
    n = 32768,
    q = 2**562,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "bfvbgv_nobootstrap_32768_quantum_192"
)

bfvbgv_nobootstrap_65536_classic_256 = LWE.Parameters(
    n = 65536,
    q = 2**920,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "bfvbgv_nobootstrap_65536_classic_256"
)

bfvbgv_nobootstrap_65536_quantum_256 = LWE.Parameters(
    n = 65536,
    q = 2**880,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "bfvbgv_nobootstrap_65536_quantum_256"
)

Table_5_4 = [
    (bfvbgv_nobootstrap_16384_classic_128, 128, classic_model),
    (bfvbgv_nobootstrap_16384_quantum_128, 128, quantum_model),
    (bfvbgv_nobootstrap_32768_classic_128, 192, classic_model),
    (bfvbgv_nobootstrap_32768_quantum_128, 192, quantum_model),
    (bfvbgv_nobootstrap_65536_classic_128, 256, classic_model),
    (bfvbgv_nobootstrap_65536_quantum_128, 256, quantum_model),
]

# Table 5.5

tfhe_742_classic_128 = LWE.Parameters(
    n = 742,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**(-17.11) * 2**64),
    m = oo,
    tag = "param_functional_tfhe_742_binary_classic_128"
)

tfhe_2048_classic_128 = LWE.Parameters(
    n = 2048,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**(-51.6) * 2**64),
    m = oo,
    tag = "tfhe_2048_classic_128"
)

tfhe_777_classic_128 = LWE.Parameters(
    n = 777,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**(-18.03) * 2**64),
    m = oo,
    tag = "tfhe_777_classic_128"
)

tfhe_1536_classic_128 = LWE.Parameters(
    n = 512 * 3,
    q = 2**64,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**(-38.08) * 2**64),
    m = oo,
    tag = "tfhe_1536_classic_128"
)

tfhe_630_classic_128 = LWE.Parameters(
    n = 630,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**(-15) * 2**32),
    m = oo,
    tag = "tfhe_630_classic_128")


tfhe_1024_classic_128 = LWE.Parameters(
    n = 1024,
    q = 2**32,
    Xs = ND.UniformMod(2),
    Xe = ND.DiscreteGaussian(2**(-25) * 2**32),
    m = oo,
    tag = "tfhe_1024_classic_128")

tfhe_512_classic_128 = LWE.Parameters(
    n = 512,
    q = 2**27,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.2),
    m = oo,
    tag = "tfhe_512_classic_128")

tfhe_1024_classic_128_27 = LWE.Parameters(
    n = 1024,
    q = 2**27,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.2),
    m = oo,
    tag = "tfhe_1024_classic_128_27")

Table_5_5 = [
    (tfhe_742_classic_128, 128, classic_model),
    (tfhe_2048_classic_128, 128, classic_model),
    (tfhe_777_classic_128, 128, classic_model),
    (tfhe_1536_classic_128, 128, classic_model),
    (tfhe_630_classic_128, 128, classic_model),
    (tfhe_1024_classic_128, 128, classic_model),
    (tfhe_512_classic_128, 128, classic_model),
    (tfhe_1024_classic_128_27, 128, classic_model)
]

#Table 5.6

ckks_nobootstrap_16384_classic_128 = LWE.Parameters(
    n = 16384,
    q = 2**426,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "ckks_nobootstrap_16384_classic_128"
)

ckks_nobootstrap_32768_classic_192 = LWE.Parameters(
    n = 32768,
    q = 2**602,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "ckks_nobootstrap_32768_classic_192"
)

ckks_nobootstrap_32768_classic_256 = LWE.Parameters(
    n = 32768,
    q = 2**472,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "ckks_nobootstrap_32768_classic_256"
)

ckks_nobootstrap_16384_quantum_128 = LWE.Parameters(
    n = 16384,
    q = 2**388,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "ckks_nobootstrap_16384_classic_128"
)

ckks_nobootstrap_32768_quantum_192 = LWE.Parameters(
    n = 32768,
    q = 2**560,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "ckks_nobootstrap_32768_classic_192"
)

ckks_nobootstrap_32768_quantum_256 = LWE.Parameters(
    n = 32768,
    q = 2**434,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "ckks_nobootstrap_32768_classic_256"
)

Table_5_6 = [
    (ckks_nobootstrap_16384_classic_128, 128, classic_model),
    (ckks_nobootstrap_32768_classic_192, 192, classic_model),
    (ckks_nobootstrap_32768_classic_256, 256, classic_model),
    (ckks_nobootstrap_16384_quantum_128, 128, quantum_model),
    (ckks_nobootstrap_32768_quantum_192, 192, quantum_model),
    (ckks_nobootstrap_32768_quantum_256, 256, quantum_model),
]


#Table 5.7

ckks_bootstrap_65536_classic_128_1 = LWE.Parameters(
    n = 65536,
    q = 2**1769,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "ckks_bootstrap_65536_classic_128"
)

ckks_bootstrap_65536_classic_128_2 = LWE.Parameters(
    n = 65536,
    q = 2**1750,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "ckks_bootstrap_65536_classic_128"
)

ckks_bootstrap_131072_classic_192 = LWE.Parameters(
    n = 131072,
    q = 2**2425,
    Xs = ND.UniformMod(3),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "ckks_bootstrap_131072_classic_128"
)

Table_5_7 = [
    (ckks_bootstrap_65536_classic_128_1, 128, classic_model),
    (ckks_bootstrap_65536_classic_128_2, 128, classic_model),
    (ckks_bootstrap_131072_classic_192, 192, classic_model),
]


