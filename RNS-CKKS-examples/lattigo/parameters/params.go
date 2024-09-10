package parameters

import (
	"fmt"
	"math"

	"github.com/tuneinsight/lattigo/v5/he/hefloat"
	"github.com/tuneinsight/lattigo/v5/ring"
	"github.com/tuneinsight/lattigo/v5/utils"
)

type SecurityType int

const (
	Classical = SecurityType(0)
)

// AssertSecurity asserts the security of the provided [hefloat.Parameters] according to the
// security parameter 2^{lambda} and security type [Classical].
// A descriptive error is returned if the parameters do not meet the target security.
func AssertSecurity(p hefloat.Parameters, lambda int, securityType SecurityType) (err error) {

	var Table map[int]map[int]int

	switch Xs := p.Xs().(type) {
	case ring.Ternary:
		if Xs.P != 2.0/3 {
			return fmt.Errorf("unsupported ternary secret-key distribution: P should be 2/3 but is %f", Xs.P)
		}

		switch securityType {
		case Classical:
			Table = TableClassicalTernary
		default:
			return fmt.Errorf("unsupported SecurityType: should be Classical but is %v", securityType)
		}

	case ring.DiscreteGaussian:
		if Xs.Sigma != 3.19 {
			return fmt.Errorf("unsupported discret Gaussian secret-key distribution: sigma should be 3.19 but is %f", Xs.Sigma)
		}

		switch securityType {
		case Classical:
			Table = TableClassicalGaussian
		default:
			return fmt.Errorf("unsupported SecurityType: should be Classical but is %v", securityType)
		}

	default:
		return fmt.Errorf("unsupported secret-key distribution: should be ring.Ternary or ring.DiscreteGaussian")
	}

	if tableLogN, ok := Table[p.LogN()]; !ok {
		return fmt.Errorf("unsupported LogN: should be %v, but is %d", utils.GetSortedKeys(Table), p.LogN())
	} else {
		if maxLogQP, ok := tableLogN[lambda]; !ok {
			return fmt.Errorf("unsupported lambda: should be %v, but is %d", utils.GetSortedKeys(Table[utils.GetSortedKeys(Table)[0]]), lambda)
		} else {
			if LogQP := math.Round(p.LogQP()); LogQP > float64(maxLogQP) {
				return fmt.Errorf("insecure parameters: p.LogQP() = %f > %f", LogQP, float64(maxLogQP))
			}
		}
	}

	return
}

// Infos prints information about the parameters.
func Infos(p hefloat.Parameters) string {
	return fmt.Sprintf(`LogN: %d 
Secret Key Distribution: %T - Density: %v
Error Distribution: %T - Sigma: %v
Base Prime Size: %d
Available Multilications: %d
Log2(PQ): %f
Log2(Q): %f
Log2(P): %f
Log2(Scaling Factor): %d`,
		p.LogN(),
		p.Xs(), p.Xs().(ring.Ternary).P,
		p.Xe(), p.Xe().(ring.DiscreteGaussian).Sigma,
		int(math.Round(math.Log2(float64(p.Q()[0])))),
		p.MaxLevel(),
		p.LogQP(),
		p.LogQ(),
		p.LogP(),
		p.LogDefaultScale())
}

// ParameterInfos is a struct storing informations about the parameters:
// - Name: Params[N]Ternary[Classic][Lambda]
// - Lambda: security (bits) of the parameters
// - SecurityType: [Classical]
type ParameterInfos struct {
	Name         string
	Lambda       int
	SecurityType SecurityType
}

// ParametersInfosList stores a list of example parameters
// ranging from N=2^15 to N=2^16, classical and quantum secure
// Lambda [128, 192, 256].
var ParametersInfosList = []ParameterInfos{
	{"Params32768TernaryClassic128", 128, Classical},
	{"Params32768TernaryClassic192", 192, Classical},
	{"Params32768TernaryClassic256", 256, Classical},
	{"Params65536TernaryClassic128", 128, Classical},
	{"Params65536TernaryClassic192", 192, Classical},
	{"Params65536TernaryClassic256", 256, Classical},
}

// ParametersList is a list of example parameters stored in a map indexed
// by their name that provide a concrete instantiation of the [ParameterInfos]
// listed in [ParametersInfosList].
var ParametersList = map[string]hefloat.ParametersLiteral{

	"Params32768TernaryClassic128": {
		LogN:            15,
		LogQ:            []int{60, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50},
		LogP:            []int{61, 61, 61},
		LogDefaultScale: 50,
	},

	"Params32768TernaryClassic192": {
		LogN:            15,
		LogQ:            []int{60, 50, 50, 50, 50, 50, 50, 50, 50},
		LogP:            []int{61, 61},
		LogDefaultScale: 50,
	},

	"Params32768TernaryClassic256": {
		LogN:            15,
		LogQ:            []int{58, 48, 48, 48, 48, 48, 48},
		LogP:            []int{58, 58},
		LogDefaultScale: 48,
	},

	"Params65536TernaryClassic128": {
		LogN:            16,
		LogQ:            []int{60, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50},
		LogP:            []int{54, 54, 54, 54, 54, 54},
		LogDefaultScale: 50,
	},

	"Params65536TernaryClassic192": {
		LogN:            16,
		LogQ:            []int{60, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50},
		LogP:            []int{54, 54, 54, 54, 54},
		LogDefaultScale: 50,
	},

	"Params65536TernaryClassic256": {
		LogN:            16,
		LogQ:            []int{60, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50},
		LogP:            []int{55, 55, 55, 54},
		LogDefaultScale: 50,
	},
}
