// Package main is a template encrypted arithmetic with floating point values, with a set of example parameters, key generation, encoding, encryption, decryption and decoding.
package main

import (
	"FHE-Security-Guidelines/RNS-CKKS-examples/lattigo/parameters"
	"fmt"
	"math"

	"github.com/tuneinsight/lattigo/v5/core/rlwe"
	"github.com/tuneinsight/lattigo/v5/he/hefloat"
)

func main() {
	var err error
	var params hefloat.Parameters

	// The user has the complete freedom when instantiating RLWE cryptographic parameters.
	// Only minimal security checks are performed (e.g. that the secret distribution does not
	// lead to a zero key).
	//
	// It is therefor the responsibility of the user to ensure that the instantiated parameters
	// are compliant with the security standard.
	//
	// This example uses the `Params32768TernaryClassic128` which provide 128-bit secure
	// parameters against classical attacks for a ring degree of 2^{15}.

	paramsLit := parameters.ParametersList["Params32768TernaryClassic128"]
	// Optional (see lattigo/schemes/ckks/parameters.go):
	// - Xs: secret-key distribution (by default ring.Ternary{P:2.0/3})
	// - Xe: error distribution (by default ring.DiscreteGaussian{Sigma:3.19, Bound:19})
	// - LogNthRoot: n-th root used (by default LogN+1)
	// - RingType:
	//   - ring.Standard (by default): Z[X]/(X^{N}+1), which enables up to N/2 complex slots
	//   - ring.ConjugateInvariant: Z[X + X^{-1}]/(X^{N} + 1), which enables up to N real slots.
	// - Q: specify exact primes (instead of LogQ)
	// - P: specify exact primes (instead of LogP)

	if params, err = hefloat.NewParametersFromLiteral(paramsLit); err != nil {
		panic(err)
	}

	// Logs information about the parameters
	fmt.Printf("\n%s\n\n", parameters.Infos(params))

	// Checks that the parameters are compliant with 128-bit classical security
	if err = parameters.AssertSecurity(params, 128, parameters.Classical); err != nil {
		panic(err)
	}

	// Key Generator
	kgen := rlwe.NewKeyGenerator(params)

	// Generate a Secret Key
	sk := kgen.GenSecretKeyNew()

	// Generate the Relinearization Key
	rlk := kgen.GenRelinearizationKeyNew(sk)

	// Galois elements for a cyclic rotation by 1 (to the left) and complex conjugation
	galEls := []uint64{params.GaloisElement(1), params.GaloisElementForComplexConjugation()}

	// Generates the Galois keys
	gks := kgen.GenGaloisKeysNew(galEls, sk)

	// Naive in memory EvaluationKeySet compliant to the [rlwe.EvaluationKeySet] interface.
	evk := rlwe.NewMemEvaluationKeySet(rlk, gks...)

	// Evaluator
	// Any struct implementing [rlwe.EvaluationKeySet] will be accepted for the keys.
	eval := hefloat.NewEvaluator(params, evk)

	// Encoder
	ecd := hefloat.NewEncoder(params)

	// Encryptor
	enc := rlwe.NewEncryptor(params, sk)

	// Decryptor
	dec := rlwe.NewDecryptor(params, sk)

	// Maximum number of slots (N/2)
	slots := params.MaxSlots()

	// Vector of plaintext values
	values := make([]complex128, slots)
	NthRoot := 32
	angle := 2 * 3.141592653589793 / float64(NthRoot)
	for i := range values {
		x := float64(i & (NthRoot - 1))
		values[i] = complex(math.Cos(angle*x), math.Sin(angle*x))
	}

	// Allocates a plaintext
	// Default rlwe.MetaData:
	// - IsBatched = true (slots encoding)
	// - Scale = params.DefaultScale()
	pt := hefloat.NewPlaintext(params, params.MaxLevel())

	// Encodes the vector on the plaintext
	if err = ecd.Encode(values, pt); err != nil {
		panic(err)
	}

	// Encrypts the plaintext
	var ct *rlwe.Ciphertext
	if ct, err = enc.EncryptNew(pt); err != nil {
		panic(err)
	}

	// Dummy encrypted circuit
	// Multiplication with relinearization
	if err = eval.MulRelin(ct, ct, ct); err != nil {
		panic(err)
	}

	// Cyclic Rotation by 1 (to the left)
	if err = eval.Rotate(ct, 1, ct); err != nil {
		panic(err)
	}

	// Complex Conjugation
	if err = eval.Conjugate(ct, ct); err != nil {
		panic(err)
	}

	// Rescaling: consumes the last prime and
	// reduces the level by 1.
	if err = eval.Rescale(ct, ct); err != nil {
		panic(err)
	}

	// Dummy plaintext circuit
	want := make([]complex128, slots)
	copy(want, values)
	for i := range want {
		x := values[(i+1)&(slots-1)]
		y := x * x
		want[i] = complex(real(y), -imag(y))
	}

	PrintPrecisionStats(params, ct, want, ecd, dec)
}

// PrintPrecisionStats decrypts, decodes and prints the precision stats of a ciphertext.
func PrintPrecisionStats(params hefloat.Parameters, ct *rlwe.Ciphertext, want []complex128, ecd *hefloat.Encoder, dec *rlwe.Decryptor) {

	var err error

	// Decrypts the vector of plaintext values
	pt := dec.DecryptNew(ct)

	// Decodes the plaintext
	have := make([]complex128, ct.Slots())
	if err = ecd.Decode(pt, have); err != nil {
		panic(err)
	}

	// Pretty prints some values
	fmt.Printf("Have: ")
	for i := 0; i < 4; i++ {
		fmt.Printf("%18.15f ", have[i])
	}
	fmt.Printf("...\n")

	fmt.Printf("Want: ")
	for i := 0; i < 4; i++ {
		fmt.Printf("%18.15f ", want[i])
	}
	fmt.Printf("...\n")

	// Pretty prints the precision stats
	fmt.Println(hefloat.GetPrecisionStats(params, ecd, dec, have, want, 0, false).String())
}
