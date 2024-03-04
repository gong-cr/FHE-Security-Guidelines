//==================================================================================
// BSD 2-Clause License
//
// Copyright (c) 2014-2022, NJIT, Duality Technologies Inc. and other contributors
//
// All rights reserved.
//
// Author TPOC: contact@openfhe.org
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright notice, this
//    list of conditions and the following disclaimer.
//
// 2. Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
// OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//==================================================================================

/*
  Simple examples for CKKS
 */

#define PROFILE

#include "openfhe.h"

using namespace lbcrypto;
// CalculateApproximationError() calculates the precision number (or approximation error).
// The higher the precision, the less the error.
double CalculateApproximationError(const std::vector<std::complex<double>>& result,
                                    const std::vector<std::complex<double>>& expectedResult) {
    if (result.size() != expectedResult.size())
        OPENFHE_THROW(config_error, "Cannot compare vectors with different numbers of elements");

    // using the average
    double accError = 0;
    for (size_t i = 0; i < result.size(); ++i) {
        accError += std::abs(result[i].real() - expectedResult[i].real());
    }
    double avrg = accError / result.size();  // get the average
    return std::abs(std::log2(avrg));
}


int main() {
    // Step 1: Setup CryptoContext

    // A. Specify main parameters
   CCParams<CryptoContextCKKSRNS> parameters;
   /*  A1) Secret key distribution
    * The secret key distribution for CKKS should either be SPARSE_TERNARY or UNIFORM_TERNARY.
    * The SPARSE_TERNARY distribution was used in the original CKKS paper,
    * but in this example, we use UNIFORM_TERNARY because this is included in the homomorphic
    * encryption standard.
    */    
   SecretKeyDist secretKeyDist = UNIFORM_TERNARY;
   parameters.SetSecretKeyDist(secretKeyDist);

   parameters.SetSecurityLevel(HEStd_NotSet);
   parameters.SetRingDim(1 << 15); //COLUMN 1,2,3,4
    // parameters.SetRingDim(1 << 16); //COLUMN 5,6   
    /* A2) Bit-length of scaling factor.
   * CKKS works for real numbers, but these numbers are encoded as integers.
   * For instance, real number m=0.01 is encoded as m'=round(m*D), where D is
   * a scheme parameter called scaling factor. Suppose D=1000, then m' is 10 (an
   * integer). Say the result of a computation based on m' is 130, then at
   * decryption, the scaling factor is removed so the user is presented with
   * the real number result of 0.13.
   *
   * Parameter 'scaleModSize' determines the bit-length of the scaling
   * factor D, but not the scaling factor itself. The latter is implementation
   * specific, and it may also vary between ciphertexts in certain versions of
   * CKKS (e.g., in FLEXIBLEAUTO).
   *
   * Choosing 'scaleModSize' depends on the desired accuracy of the
   * computation, as well as the remaining parameters like multDepth or security
   * standard. This is because the remaining parameters determine how much noise
   * will be incurred during the computation (remember CKKS is an approximate
   * scheme that incurs small amounts of noise with every operation). The
   * scaling factor should be large enough to both accommodate this noise and
   * support results that match the desired accuracy.
   */
   
    ScalingTechnique rescaleTech = FLEXIBLEAUTO;
    usint scaleModSize               = 50;
    usint firstMod               = 60; //COLUMN 1,2,3
    // usint firstMod               = 61; //COLUMN 4,6
    // usint firstMod               = 67; //COLUMN 5


    /* A4) Desired security level based on FHE standards.
   * This parameter can take four values. Three of the possible values
   * correspond to 128-bit, 192-bit, and 256-bit security, and the fourth value
   * corresponds to "NotSet", which means that the user is responsible for
   * choosing security parameters. Naturally, "NotSet" should be used only in
   * non-production environments, or by experts who understand the security
   * implications of their choices.
   *
   * If a given security level is selected, the library will consult the current
   * security parameter tables defined by the FHE standards consortium
   * (https://homomorphicencryption.org/introduction/) to automatically
   * select the security parameters. Please see "TABLES of RECOMMENDED
   * PARAMETERS" in  the following reference for more details:
   * http://homomorphicencryption.org/wp-content/uploads/2018/11/HomomorphicEncryptionStandardv1.1.pdf
   */
    parameters.SetScalingModSize(scaleModSize);
    parameters.SetScalingTechnique(rescaleTech);
    parameters.SetFirstModSize(firstMod);
    
    usint depth = 5;
    parameters.SetMultiplicativeDepth(depth);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    // Enable the features that you wish to use
    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);
    cc->Enable(ADVANCEDSHE);
    cc->Enable(FHE);
   /*A3) Number of plaintext slots used in the ciphertext.
   * CKKS packs multiple plaintext values in each ciphertext.
   * The maximum number of slots depends on a security parameter called ring
   * dimension. */
  /*
   * Please use method GetRingDimension() to find out the exact ring dimension
   * being used for these parameters. Give ring dimension N, the maximum batch
   * size is N/2, because of the way CKKS works.
   */
    usint ringDim = cc->GetRingDimension();
    std::cout << "CKKS scheme is using ring dimension " << ringDim << std::endl << std::endl;
    uint32_t batchSize = ringDim/2;
    // B. Step 2: Key Generation
    /* B1) Generate encryption keys.
   * These are used for encryption/decryption, as well as in generating
   * different kinds of keys.
   */
    auto keys = cc->KeyGen();

    /* B2) Generate the digit size
   * In CKKS, whenever someone multiplies two ciphertexts encrypted with key s,
   * we get a result with some components that are valid under key s, and
   * with an additional component that's valid under key s^2.
   *
   * In most cases, we want to perform relinearization of the multiplicaiton
   * result, i.e., we want to transform the s^2 component of the ciphertext so
   * it becomes valid under original key s. To do so, we need to create what we
   * call a relinearization key with the following line.
   */
    cc->EvalMultKeyGen(keys.secretKey);

    /* B3) Generate the rotation keys
   * CKKS supports rotating the contents of a packed ciphertext, but to do so,
   * we need to create what we call a rotation key. This is done with the
   * following call, which takes as input a vector with indices that correspond
   * to the rotation offset we want to support. Negative indices correspond to
   * right shift and positive to left shift. Look at the output of this demo for
   * an illustration of this.
   *
   * Keep in mind that rotations work over the batch size or entire ring dimension (if the batch size is not specified).
   * This means that, if ring dimension is 8 and batch
   * size is not specified, then an input (1,2,3,4,0,0,0,0) rotated by 2 will become
   * (3,4,0,0,0,0,1,2) and not (3,4,1,2,0,0,0,0).
   * If ring dimension is 8 and batch
   * size is set to 4, then the rotation of (1,2,3,4) by 2 will become (3,4,1,2).
   * Also, as someone can observe
   * in the output of this demo, since CKKS is approximate, zeros are not exact
   * - they're just very small numbers.
   */
    // cc->EvalRotateKeyGen(keys.secretKey, {1, -2});

    // Step 3: Encoding and encryption of inputs

    // Inputs (adopted from https://github.com/microsoft/SEAL/blob/main/native/examples/5_ckks_basics.cpp)
    // Copyright (c) Microsoft Corporation. All rights reserved.
    // Licensed under the MIT license

    double step_size = 1.0/(static_cast<double>(batchSize) - 1);
    std::vector<double> x1;
    x1.reserve(batchSize);
    double curr_point = 0;
    for (size_t i = 0; i < batchSize; i++)
    {
        x1.push_back(curr_point);
        curr_point += step_size;
    }
    // std::vector<double> x1 = {0.25, 0.5, 0.75, 1.0, 2.0, 3.0, 4.0, 5.0};
    // Encoding as plaintexts
    Plaintext ptxt1 = cc->MakeCKKSPackedPlaintext(x1);

    // std::cout << "Input x1: " << ptxt1 << std::endl;

    // Encrypt the encoded vectors
    auto c1 = cc->Encrypt(keys.publicKey, ptxt1);
    auto c0 = cc->Encrypt(keys.publicKey, ptxt1);
    // Step 4: Evaluation

    // Homomorphic multiplication
    uint32_t mul_depth = depth;
    std::cout<<"c1 level=" << c1->GetLevel() << std::endl;

    for (uint32_t i = 0; i < mul_depth; i++){
      // c1 = cc->EvalMult(c1, c1);
      // std::cout<<"co"<<c0;
      c1 = cc->EvalMult(c1, c0);
      std::cout<<"i= "<<i<<" c1 level=" << c1->GetLevel() << std::endl;
      std::cout<<"i= "<<i<<" after rescaling c1 level=" << c1->GetLevel() << std::endl;
    }
    
    std::vector<double> expectedResult;
    std::cout << "cleartext results = ";
    for (double entry : x1) {
        double expectedEntry = std::pow(entry, mul_depth+1);//std::pow(2, mul_depth)
        expectedResult.push_back(expectedEntry);
        // std::cout << expectedEntry << ' ';
    }
    
    std::cout << std::endl;
    Plaintext ptxt_expResult = cc->MakeCKKSPackedPlaintext(expectedResult);
    // std::cout<<"c1 level=" << c1->GetLevel() << std::endl;
    // auto cMul = cc->EvalMult(c1, c1);
    // std::cout<<"cMul level=" << cMul->GetLevel() << std::endl;
    // auto cMul2 = cc->EvalMult(cMul, cMul);
    // std::cout<<"cMul2 level=" << cMul2->GetLevel() << std::endl;
    

    // Step 5: Decryption and output
    Plaintext result;
    // We set the cout precision to 8 decimal digits for a nicer output.
    // If you want to see the error/noise introduced by CKKS, bump it up
    // to 15 and it should become visible.
    std::cout.precision(50);

    std::cout << std::endl << "Results of homomorphic computations: " << std::endl;
    std::cout<<__LINE__<<std::endl;
    cc->Decrypt(keys.secretKey, c1, &result);
    std::cout<<__LINE__<<std::endl;
    result->SetLength(batchSize);
    std::cout<<__LINE__<<std::endl;
    // std::cout << "computed results = " << result;
    std::cout << "Estimated precision in bits: " << result->GetLogPrecision() << std::endl;

    // // Decrypt the result of multiplication
    // cc->Decrypt(keys.secretKey, c1, &result);
    // result->SetLength(batchSize);
    // std::cout << "actual result " << result << std::endl;

    auto actualResult = result->GetCKKSPackedValue();
    double precision = CalculateApproximationError(actualResult, ptxt_expResult->GetCKKSPackedValue());
    std::cout << "Real precision in bits: " << precision << std::endl;
    return 0;
}
