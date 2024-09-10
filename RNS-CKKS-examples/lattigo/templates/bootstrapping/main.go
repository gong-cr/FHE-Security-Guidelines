// Package main implements an example showcasing the basics of the bootstrapping for fixed-point approximate arithmetic over the reals/complexes.
// The bootstrapping is a circuit that homomorphically re-encrypts a ciphertext at level zero to a ciphertext at a higher level, enabling further computations.
// Note that, unlike other bootstrappings (BGV/BFV/TFHE), the this bootstrapping does not reduce the error in the ciphertext, but only enables further computations.
// This example shows how to bootstrap a single ciphertext whose ring degree is the same as the one of the bootstrapping parameters.
// Use the flag -short to run the examples fast but with insecure parameters.
//
// This example requires 24GB of memory to run with 128-bit secure parameters (LogN=16).
package main

import (
	"flag"
	"fmt"
	"math"
	"time"

	"FHE-Security-Guidelines/RNS-CKKS-examples/lattigo/parameters"
	"FHE-Security-Guidelines/RNS-CKKS-examples/lattigo/templates/bootstrapping/failure"

	"github.com/tuneinsight/lattigo/v5/core/rlwe"
	"github.com/tuneinsight/lattigo/v5/he/hefloat"
	"github.com/tuneinsight/lattigo/v5/he/hefloat/bootstrapping"
	"github.com/tuneinsight/lattigo/v5/ring"
	"github.com/tuneinsight/lattigo/v5/utils"
)

var flagShort = flag.Bool("short", false, "run the example with a smaller and insecure ring degree.")

type Parameters struct {
	ResidualLit      hefloat.ParametersLiteral
	BootstrappingLit bootstrapping.ParametersLiteral
}

var ParametersClassical = map[int]Parameters{
	128: {

		// First we must define the residual parameters.
		// The residual parameters are the parameters used outside of the bootstrapping circuit.
		ResidualLit: hefloat.ParametersLiteral{
			LogN:            16,                                                // Log2 of the ring degree
			LogQ:            []int{45, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35}, // Log2 of the ciphertext prime moduli
			LogP:            []int{55, 40, 40},                                 // Log2 of the key-switch auxiliary prime moduli
			LogDefaultScale: 35,                                                // Log2 of the scale
		},

		// The bootstrapping circuit use its own Parameters
		// which will be automatically instantiated given
		// the residual parameters and the bootstrapping parameters.

		// !WARNING! The bootstrapping parameters are not ensured to
		// be 128-bit secure, it is the responsibility of the user
		// to check that the meet the security requirement and tweak
		// them if necessary.

		// In this example we need to specify multiple advanced parameters
		// for the bootstrapping to work since we are constrainted to use
		// a secret with density 2/3.
		BootstrappingLit: bootstrapping.ParametersLiteral{
			// We specify LogN to ensure that both the residual
			// parameters and the bootstrapping parameters have
			// the same LogN. This is not required, but we want
			// it for this example.
			LogN: utils.Pointy(16),

			// In this example we manually specify the
			// bootstrapping parameters' secret distribution.
			// This is not necessary, but we ensure here that
			// they are the same as the residual parameters.
			Xs: ring.Ternary{P: 2 / 3.0},

			// By default the Sparse-Secret Encapsulation technique of
			// https://eprint.iacr.org/2022/024 is used, so we manually
			// set it to 0 to not use it.
			EphemeralSecretWeight: utils.Pointy(0),

			// The default values for the following fields is set for
			// an expected precision of ~27.5 bits, however since we are
			// constrained to a dense secrete, the final precision is closer
			// to ~16 bits, so the size of the prime moduli can be reduced
			// to gain some more homomorphic capacity to allocate to the
			// residual parameters.
			SlotsToCoeffsFactorizationDepthAndLogScales: [][]int{{30}, {30}, {30}},

			K: utils.Pointy(512),
			// We then need adapt the approximation of the homomorphic
			// modular reduction accordingly.
			Mod1Type:    hefloat.CosContinuous,
			Mod1Degree:  utils.Pointy(255),
			DoubleAngle: utils.Pointy(4),
		},
	},
}

func main() {

	flag.Parse()

	ResidualLit := ParametersClassical[128].ResidualLit
	BootstrappingLit := ParametersClassical[128].BootstrappingLit

	if *flagShort {
		ResidualLit.LogN -= 2
		BootstrappingLit.LogN = utils.Pointy(ResidualLit.LogN)
	}

	//==============================
	//=== 1) RESIDUAL PARAMETERS ===
	//==============================

	params, err := hefloat.NewParametersFromLiteral(ResidualLit)

	if err != nil {
		panic(err)
	}

	//==========================================
	//=== 2) BOOTSTRAPPING PARAMETERSLITERAL ===
	//==========================================

	// We can estimate the bootstrapping failure probability with:
	fmt.Println("==== FAILURE PROBABILITY ====")
	Xs := params.Xs().(ring.Ternary)
	pr := failure.Probability(&Xs, *BootstrappingLit.K, params.LogN(), params.LogMaxSlots())
	fmt.Printf("Failure Probability given K=%d: 2^{%f}\n", *BootstrappingLit.K, pr)
	fmt.Println("=============================")

	//===================================
	//=== 3) BOOTSTRAPPING PARAMETERS ===
	//===================================

	// Now that the residual parameters and the bootstrapping parameters
	// literals are defined, we can instantiate the bootstrapping parameters.
	// The instantiated bootstrapping parameters store their own hefloat.Parameter,
	// which are the parameters of the ring used by the bootstrapping circuit.
	// The bootstrapping parameters are a wrapper of hefloat.Parameters,
	// with additional information.
	// They therefore has the same API as the hefloat.Parameters
	// and we can use this API to print some information.
	btpParams, err := bootstrapping.NewParametersFromLiteral(params, BootstrappingLit)
	if err != nil {
		panic(err)
	}

	if *flagShort {
		// Corrects the message ratio Q0/|m(X)| to take into account the
		// smaller number of slots and keep the same precision
		btpParams.Mod1ParametersLiteral.LogMessageRatio += 16 - params.LogN()
	}

	// Logs information about the residual parameters
	fmt.Printf("\nResidual Parameters\n%s\n\n", parameters.Infos(params))

	// Checks that the residual parameters are compliant with 128-bit classical security
	if err = parameters.AssertSecurity(params, 128, parameters.Classical); err != nil {
		if *flagShort {
			fmt.Printf("warning: %s\n\n", err)
		} else {
			panic(err)
		}
	}

	// Logs information about the bootstrapping parameters
	fmt.Printf("\n Bootstrapping Parameters\n%s\n\n", parameters.Infos(btpParams.BootstrappingParameters))

	// Checks that the bootstrapping parameters are compliant with 128-bit classical security
	if err = parameters.AssertSecurity(btpParams.BootstrappingParameters, 128, parameters.Classical); err != nil {
		if *flagShort {
			fmt.Printf("warning: %s\n\n", err)
		} else {
			panic(err)
		}
	} //

	//==============================
	//=== 4) KEYGEN & ENCRYPTION ===
	//==============================

	// Now that both the residual and bootstrapping parameters are instantiated, we can
	// instantiate the usual necessary object to encode, encrypt and decrypt.

	// Scheme context and keys
	kgen := rlwe.NewKeyGenerator(params)

	sk, pk := kgen.GenKeyPairNew()

	encoder := hefloat.NewEncoder(params)
	decryptor := rlwe.NewDecryptor(params, sk)
	encryptor := rlwe.NewEncryptor(params, pk)

	fmt.Println()
	fmt.Println("Generating bootstrapping evaluation keys...")
	evk, _, err := btpParams.GenEvaluationKeys(sk)
	if err != nil {
		panic(err)
	}
	fmt.Println("Done")

	//========================
	//=== 5) BOOTSTRAPPING ===
	//========================

	// Instantiates the bootstrapper
	var eval *bootstrapping.Evaluator
	if eval, err = bootstrapping.NewEvaluator(btpParams, evk); err != nil {
		panic(err)
	}

	// Generate a random plaintext with values uniformely distributed
	// in [-1, 1] for the real and imaginary part.
	slots := params.MaxSlots()
	valuesWant := make([]complex128, params.MaxSlots())
	for i := range valuesWant {
		valuesWant[i] = complex(float64(i)/float64(slots-1), float64(i)/float64(slots-1))
	}

	// We encrypt at level 0
	plaintext := hefloat.NewPlaintext(params, 0)
	if err := encoder.Encode(valuesWant, plaintext); err != nil {
		panic(err)
	}

	// Encrypt
	ciphertext1, err := encryptor.EncryptNew(plaintext)
	if err != nil {
		panic(err)
	}

	// Decrypt, print and compare with the plaintext values
	fmt.Println()
	fmt.Println("Precision of values vs. ciphertext")
	valuesTest1 := printDebug(params, ciphertext1, valuesWant, decryptor, encoder)

	// Bootstrap the ciphertext (homomorphic re-encryption)
	// It takes a ciphertext at level 0 (if not at level 0, then it will reduce it to level 0)
	// and returns a ciphertext with the max level of `floatParamsResidualLit`.
	// CAUTION: the scale of the ciphertext MUST be equal (or very close) to params.DefaultScale()
	// To equalize the scale, the function evaluator.SetScale(ciphertext, parameters.DefaultScale()) can be used at the expense of one level.
	// If the ciphertext is is at level one or greater when given to the bootstrapper, this equalization is automatically done.
	fmt.Println("Bootstrapping...")
	now := time.Now()
	ciphertext2, err := eval.Bootstrap(ciphertext1)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Done: %s\n", time.Since(now))

	//=====================
	//=== 6) DECRYPTION ===
	//=====================

	// Decrypt, print and compare with the plaintext values
	fmt.Println()
	fmt.Println("Precision of ciphertext vs. Bootstrap(ciphertext)")
	printDebug(params, ciphertext2, valuesTest1, decryptor, encoder)
}

func printDebug(params hefloat.Parameters, ciphertext *rlwe.Ciphertext, valuesWant []complex128, decryptor *rlwe.Decryptor, encoder *hefloat.Encoder) (valuesTest []complex128) {

	valuesTest = make([]complex128, ciphertext.Slots())

	if err := encoder.Decode(decryptor.DecryptNew(ciphertext), valuesTest); err != nil {
		panic(err)
	}

	fmt.Println()
	fmt.Printf("Level: %d (logQ = %d)\n", ciphertext.Level(), params.LogQLvl(ciphertext.Level()))

	fmt.Printf("Scale: 2^%f\n", math.Log2(ciphertext.Scale.Float64()))
	fmt.Printf("ValuesTest: %6.10f %6.10f %6.10f %6.10f...\n", valuesTest[0], valuesTest[1], valuesTest[2], valuesTest[3])
	fmt.Printf("ValuesWant: %6.10f %6.10f %6.10f %6.10f...\n", valuesWant[0], valuesWant[1], valuesWant[2], valuesWant[3])

	precStats := hefloat.GetPrecisionStats(params, encoder, nil, valuesWant, valuesTest, 0, false)

	fmt.Println(precStats.String())
	fmt.Println()

	return
}
