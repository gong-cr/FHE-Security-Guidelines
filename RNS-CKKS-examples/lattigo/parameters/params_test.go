package parameters

import (
	"testing"

	"github.com/tuneinsight/lattigo/v5/he/hefloat"
)

// TestExampleParams checks that all parameters listed
// in ParametersInfosList meet their security target.
func TestExampleParams(t *testing.T) {

	for _, paramsInfos := range ParametersInfosList {

		name := paramsInfos.Name

		t.Logf("%s\n", name)
		p, err := hefloat.NewParametersFromLiteral(ParametersList[name])
		if err != nil {
			t.Fatal(err)
		}

		t.Log(Infos(p))

		if err := AssertSecurity(p, paramsInfos.Lambda, paramsInfos.SecurityType); err != nil {
			t.Fatal(err)
		}
	}

}
