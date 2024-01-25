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
    n = 65536,
    q = 2**1206,
    Xs = ND.SparseTernary(65536, 4096, 4096),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_ternary8192_classic_192"
)

param_functional_65536_ternary8192_classic_256 = LWE.Parameters(
    n = 65536,
    q = 2**918,
    Xs = ND.SparseTernary(65536, 4096, 4096),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_ternary21845_classic_256"
)

param_functional_32768_ternary21845_quantum_128 = LWE.Parameters(
    n = 32768,
    q = 2**825,
    Xs = ND.SparseTernary(32768, 10922, 10923),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_32768_ternary21845_quantum_128"
)

param_functional_65536_ternary8192_quantum_192 = LWE.Parameters(
    n = 65536,
    q = 2**1139,
    Xs = ND.SparseTernary(65536, 4096, 4096),
    Xe = ND.DiscreteGaussian(3.19),
    m = oo,
    tag = "param_functional_65536_ternary8192_quantum_192"
)

param_functional_65536_ternary8192_quantum_256 = LWE.Parameters(
    n = 65536,
    q = 2**866,
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

