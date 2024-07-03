package failure

import (
	"fmt"
	"math"
	"math/big"

	"github.com/tuneinsight/lattigo/v5/ring"
	"github.com/tuneinsight/lattigo/v5/utils/bignum"
)

// Probability returns the probability that PR[||I(X)|| > K].
// - Xs: secret distribution
// - K: upper bound for I(X)
// - logN: log2(ring degree)
// - logSlots: log2(#complex slots)
func Probability(Xs *ring.Ternary, K, logN, logSlots int) (logfailure float64) {

	// failureProbability returns PR[||I(X)|| > K] given
	// h: the Hamming weight of the secret
	// K: the upper bound of I(X)
	// logSlots: log2(#complex slots)

	if Xs.H != 0 && Xs.P != 0 {
		panic(fmt.Errorf("invalid Xs: Xs.H and Xs.P cannot both be non-zero"))
	}

	var c int
	var Eh int

	// If Xs is a probability density, then also takes into account
	// the correction factor of K.
	if Xs.P != 0 {

		prec := uint(256)

		N := math.Exp2(float64(logN))
		Eh = int(math.Ceil(N*Xs.P) + 1)

		EhSqrt := math.Sqrt(float64(Eh))
		s := math.Sqrt(1 - Xs.P)
		sqrt2 := math.Sqrt(2)

		// Binary search such that |PR[I(X) > K - c] - PR[h > E[h] + c/kappa * sigma(h)]| is small
		c = K >> 1
		step := c >> 1
		for step != 0 {

			kappa := float64(K-c) / EhSqrt
			d := float64(c) / (kappa * s)
			erfc := Log2ErfC(d/sqrt2, prec)
			fail := failureProbability(Eh, K-c, logSlots)

			if erfc > fail {
				c += step
			} else if erfc < fail {
				c -= step
			} else {
				break
			}

			step >>= 1
		}

	} else {
		Eh = Xs.H
	}

	return failureProbability(Eh, K-c, logSlots)
}

// failureProbability returns PR[||I(X)|| > K] given
// h: the Hamming weight of the secret
// K: the upper bound of I(X)
// logSlots: log2(#complex slots)
func failureProbability(h, K, logSlots int) (logfailure float64) {
	if h > 1024 {
		kappa := float64(K) / math.Sqrt(float64(h))
		return F8192[int(math.Round(math.Sqrt(8192+1)*kappa))] + float64(logSlots+1)
	}

	return ModifiedIrwinHall(K, h, logSlots)
}

// FindSuitableK finds the smallest K such that PR[||I(X)|| > K] <= 2^{logfailure}.
func FindSuitableK(Xs *ring.Ternary, logN, logSlots int, logfailure float64) (K int) {

	// getCorrectionFactor returns d such that 1-erf(d/sqrt(2))
	// is close to 2^{logfailure}.
	getCorrectionFactor := func(logfailure float64) (d float64) {

		prec := uint(256)

		sqrt2 := math.Sqrt(2)

		d = 1.0
		for Log2ErfC(d/sqrt2, prec) > logfailure {
			d++
		}

		step := d
		for step > 1e-3 {

			if Log2ErfC(d/sqrt2, prec) > logfailure {
				d += step
			} else {
				d -= step
			}

			step /= 2
		}

		return
	}

	findK := func(h, logSlots int, logfailure float64) (K int) {

		if h > 1024 {
			K = len(F8192) >> 1
			step := K >> 1
			for step > 0 {
				if F8192[K] > logfailure-float64(logSlots+1) {
					K += step
				} else if F8192[K] < logfailure-float64(logSlots+1) {
					K -= step
				} else {
					break
				}

				step >>= 1
			}

			for F8192[K] < logfailure-float64(logSlots+1) {
				K--
			}

			for F8192[K] > logfailure-float64(logSlots+1) {
				K++
			}

			kappa := float64(K) / math.Sqrt(float64(8192+1))

			return int(math.Ceil(kappa * math.Sqrt(float64(h+1))))
		} else {

			step := h >> 2
			K = h >> 1
			for step > 0 {

				if d := ModifiedIrwinHall(K, h, logSlots); d > logfailure {
					K += step
				} else if d < logfailure {
					K -= step
				} else {
					return
				}

				step >>= 1
			}

			for ModifiedIrwinHall(K, h, logSlots) < logfailure {
				K--
			}

			for ModifiedIrwinHall(K, h, logSlots) > logfailure {
				K++
			}

			return
		}

	}

	if Xs.H != 0 && Xs.P != 0 {
		panic(fmt.Errorf("invalid Xs: Xs.H and Xs.P cannot both be non-zero"))
	}

	if Xs.H != 0 {
		return findK(Xs.H, logSlots, logfailure)
	}

	// If Xs is a probability density, then also
	// adds a correction factor to K.
	N := math.Exp2(float64(logN))

	Eh := math.Ceil(N*Xs.P) + 1

	K = findK(int(Eh), logSlots, logfailure)

	kappa := float64(K) / math.Sqrt(Eh)

	d := getCorrectionFactor(logfailure)

	return K + int(math.Ceil(d*kappa*math.Sqrt(1-Xs.P)))
}

// Log2ErfC returns log2(1 - erf(x)).
func Log2ErfC(x float64, prec uint) (rF64 float64) {

	// Implements erfByEquation2 & erfcByEquation3
	// of "The functions erf and erfc computed with
	// arbitrary precision  and explicit error bounds"
	// from S. Chevillard.
	N := int(prec)

	L := int(math.Ceil(math.Sqrt(float64(N))))

	S := make([]*big.Float, L)
	for i := range S {
		S[i] = new(big.Float).SetPrec(prec)
	}

	xBig := new(big.Float).SetPrec(prec).SetFloat64(x)

	var y *big.Float

	t := 10.0

	if x > t {
		// acc <- x * x
		acc := new(big.Float).Mul(xBig, xBig)

		// y <- 1/(2*acc)
		y = new(big.Float).Add(acc, acc)
		y.Quo(new(big.Float).SetPrec(1), y)

		// acc <- exp(-acc)
		acc.Neg(acc)
		acc = bignum.Exp(acc)

		// tmp <- x * sqrt(pi)
		tmp := bignum.Pi(prec)
		tmp.Sqrt(tmp)
		tmp.Mul(xBig, tmp)

		// acc <- acc / tmp
		acc.Quo(acc, tmp)

		z := bignum.Pow(y, new(big.Float).SetPrec(prec).SetFloat64(float64(L)))

		for k, i := 0, 0; k <= N; k++ {

			if k&1 == 0 {
				S[i].Add(S[i], acc)
			} else {
				S[i].Sub(S[i], acc)
			}

			if i == L-1 {
				i = 0
				acc.Mul(acc, z)
			} else {
				i++
			}

			acc.Mul(acc, new(big.Float).SetPrec(prec).SetInt64(int64(2*k-1)))
		}

	} else {

		// y <- 2 * x * x
		y = new(big.Float).Mul(xBig, xBig)
		y.Add(y, y)
		z := bignum.Pow(y, new(big.Float).SetPrec(prec).SetFloat64(float64(L)))

		// acc <- 2*x/sqrt(pi)
		acc := bignum.Pi(prec)
		acc.Sqrt(acc)
		acc.Quo(xBig, acc)
		acc.Add(acc, acc)

		// tmp <- exp(-x^2)
		tmp := new(big.Float).Mul(xBig, xBig)
		tmp.Neg(tmp)
		tmp = bignum.Exp(tmp)

		// acc <- 2*x/sqrt(pi) * exp(-x^2)
		acc.Mul(acc, tmp)

		for k, i := 1, 0; k <= N; k++ {
			S[i].Add(S[i], acc)

			if i == L-1 {
				i = 0
				acc.Mul(acc, z)
			} else {
				i++
			}
			acc.Quo(acc, new(big.Float).SetPrec(prec).SetInt64(int64(2*k+1)))
		}
	}

	r := S[L-1]
	for i := L - 2; i >= 0; i-- {
		r.Mul(r, y)
		r.Add(r, S[i])
	}

	if x <= t {
		r.Sub(new(big.Float).SetPrec(prec).SetInt64(1), r)
	}

	r = bignum.Log(r)
	r.Quo(r, bignum.Log2(prec))

	rF64, _ = r.Float64()

	return rF64
}
