# FHE SECURIT GUIDELINES - RNS-CKKS - LATTIGO

This is the complementary code to [Security Guidelines for Implementing Homomorphic Encryption](https://eprint.iacr.org/2024/463).

It implements code for [Lattigo](https://github.com/tuneinsight/lattigo) to assert the security of `hefloat.Parameters`, provides example parameters and concrete instantiations of SHE and FHE CKKS instances, as well as methods to estimate the failure probability of the CKKS bootstrapping.

## `./parameters`

Method and tables to assert the security of parameters.

## `./templates`

Example of parameters instantiations for SHE (`basic`) and FHE `(bootstrapping`).

## `./templates/bootstrapping/failure`

Methods to estimate the bootstrapping failure probability and find suitable parameters.