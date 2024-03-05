package failure

import (
	"fmt"
	"math"
	"math/big"

	"github.com/tuneinsight/lattigo/v5/utils"
	"github.com/tuneinsight/lattigo/v5/utils/bignum"
)

// FindSuitable finds the smallest K such that PR[||I(X)|| > K] <= 2^{logfailure}
// Result is exact for h <= 4096 and approximate for h > 4096.
func FindSuitableK(h, logSlots int, logfailure float64) (K int) {
	if h <= 4096 {

		K = h >> 1

		step := K >> 1

		for step > 0 {

			pr := BootstrappingFailureProbability(K, h, logSlots)

			//fmt.Printf("PR[||I(X)|| > K=%d] = 2^{%f}\n", K, pr)

			if pr > logfailure {
				K += step
			} else {
				K -= step
			}

			step >>= 1
		}

		pr := BootstrappingFailureProbability(K, h, logSlots)

		//fmt.Printf("PR[||I(X)|| > K=%d] = 2^{%f}\n", K, pr)

		if pr > logfailure {
			K++
		} else if pr < logfailure {
			K--
			if BootstrappingFailureProbability(K, h, logSlots) > logfailure {
				K++
			}
		}

		//fmt.Printf("PR[||I(X)|| > K=%d] = 2^{%f}\n", K, pr)

		return K

	} else {
		return int(float64(FindSuitableK(4096, logSlots, logfailure))/math.Sqrt(float64(4097))*math.Sqrt(float64(h+1)) + 1)
	}
}

// FailureProbability estimates PR[||I(X)|| > K] by evaluating equation (1) of https://eprint.iacr.org/2022/024:
// 1 - (2/(h+1)! * (sum_i=0^{K+0.5(h+1)} (-1)^i * binom(h+1, i) * (K + 0.5(h+1) - i)^{h+1}))-1)^{2n}
// This method is numerically stable and produces accurate results, but is O(h^3).
func BootstrappingFailureProbability(K, h, logSlots int) (logfailure float64) {

	var prec uint = utils.Max(uint(2*h), 512)

	sum := new(big.Float).SetPrec(prec)

	two := new(big.Float).SetPrec(prec).SetInt64(2)
	one := new(big.Float).SetPrec(prec).SetInt64(1)
	binom := new(big.Float).Set(one)

	for i := 0; i < K+(h+1)>>1; i++ {

		// binom(h+1, i)
		if i > 0 {
			binom.Mul(binom, new(big.Float).SetPrec(prec).SetInt64(int64(h+2-i)))
			binom.Quo(binom, new(big.Float).SetPrec(prec).SetInt64(int64(i)))
		}

		// 2 * (K + 0.5(h+1) - i)^(h+1) / (h+1)!
		x := new(big.Float).SetPrec(prec).SetFloat64(float64(K) + 0.5*float64(h+1) - float64(i))
		y := new(big.Float).Set(one)
		for j := 0; j < h+1; j++ {
			y.Mul(y, x)
			y.Quo(y, new(big.Float).SetPrec(prec).SetInt64(int64(j+1)))
		}

		// binom(h+1, i) * 2 * (K + 0.5(h+1) - i)^(h+1) / (h+1)!
		y.Mul(y, binom)

		if i&1 == 0 {
			sum.Add(sum, y)
		} else {
			sum.Sub(sum, y)
		}
	}

	sum.Mul(sum, two)
	sum.Sub(sum, one)
	sum.Sub(one, sum)

	if sum.Cmp(new(big.Float)) == -1 {
		return math.Inf(-1)
	}

	sum = bignum.Log(sum)
	sum.Quo(sum, bignum.Log2(prec))
	sumF64, _ := sum.Float64()
	return sumF64 + 1 + float64(logSlots)
}
