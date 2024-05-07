# FHE SECURIT GUIDELINES - RNS-CKKS - LATTIGO

This is the complementary code to [Security Guidelines for Implementing Homomorphic Encryption](https://eprint.iacr.org/2024/463).

It implements code for [Lattigo](https://github.com/tuneinsight/lattigo) to assert the security of `hefloat.Parameters`, provides example parameters and concrete instantiations of SHE and FHE CKKS instances, as well as methods to estimate the failure probability of the CKKS bootstrapping.

## SETUP

1. Install Go: https://go.dev/
2. Check that Go was installed properly and added to the `PATH` with `$ go version`
3. Clone the repository https://github.com/gong-cr/FHE-Security-Guidelines
4. `$ cd RNS-CKKS-examples/lattigo`
5. `$ go test ./...` (this will run the tests and download all the dependencies)

## ORGANIZATION
- `./parameters`: Methods and tables to assert the security of parameters.
- `./templates/basic`: Example of parameters instantiation for SHE.
- `./templates/bootstrapping`: Example of parameters instantiation for FHE.
- `./templates/bootstrapping/failure`: Methods to estimate the bootstrapping failure probability and find suitable parameters for a target failure probability.

## RUNNING EXAMPLES

To run a specific examples, go into the appropriate folder and `$ go run main.go`.
For example, to run the FHE (`bootstrapping`) example:
1. `$ cd templates/bootstrapping`
2. `$ go run main.go`

## WARNING

Some example might require up to ~24GB of RAM, documentation can be found at the top of each `main.go` file.