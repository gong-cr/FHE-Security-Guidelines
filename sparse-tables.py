## TODO: remove this section?
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

## TODO: remove this section?
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

## TODO: remove this section?
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