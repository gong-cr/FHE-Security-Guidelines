To generate the output parameters, cd into `/FHE-Security-Guidelines/TFHE-examples/concrete/compilers/concrete-optimizer` and run the command in `command.txt`:

```
cargo run --release --quiet --bin v0-parameters -- $@ --p-error=5.421010862427522e-20 --min-precision=4 --max-precision=4
```

this will generate 128-bit secure parameters with a failure probability of `2^(-64)`, and you will recieve the output:

```
security level: 128
target p_error: 5.4e-20
per precision and log norm2:

  - 4: # bits
    -ln2:   k,  N,    n, br_l,br_b, ks_l,ks_b,  cost, p_error
    - 0 :   1, 11,  805,    1, 23,     5,  3,    105, 4.1e-20
    - 1 :   1, 11,  805,    1, 23,     5,  3,    105, 4.4e-20
    - 2 :   1, 11,  806,    1, 23,     5,  3,    105, 3.9e-20
    - 3 :   1, 11,  809,    1, 23,     5,  3,    105, 3.9e-20
    - 4 :   1, 11,  826,    1, 23,     5,  3,    108, 5.1e-20
    - 5 :   1, 11,  805,    2, 15,     5,  3,    149, 4.0e-20
    - 6 :   1, 11,  805,    2, 15,     5,  3,    149, 4.0e-20
    - 7 :   1, 11,  805,    2, 15,     5,  3,    149, 4.1e-20
    - 8 :   1, 11,  805,    2, 15,     5,  3,    149, 4.2e-20
    - 9 :   1, 11,  805,    2, 15,     5,  3,    149, 5.0e-20
    - 10:   1, 11,  807,    2, 15,     5,  3,    149, 4.8e-20
    - 11:   1, 11,  817,    2, 15,     5,  3,    151, 4.3e-20
    - 12:   1, 11,  805,    3, 11,     5,  3,    193, 4.7e-20
    - 13:   1, 11,  806,    3, 11,     5,  3,    193, 5.2e-20
    - 14:   1, 11,  812,    3, 11,     5,  3,    195, 4.9e-20
    - 15:   1, 11,  816,    3, 11,    16,  1,    231, 5.3e-20
    - 16:   1, 11,  809,    4,  9,     5,  3,    238, 3.9e-20
    - 17:   1, 11,  793,    4,  9,     8,  2,    243, 5.2e-20
    - 18:   1, 11,  790,    5,  8,     8,  2,    285, 4.8e-20
    - 19:   1, 11,  794,    6,  7,     8,  2,    330, 4.3e-20
    - 20:   1, 11,  798,    7,  6,     8,  2,    375, 4.8e-20
    - 21:   1, 11,  821,    8,  5,     8,  2,    431, 5.4e-20
    - 22:   1, 11,  819,   11,  4,    17,  1,    593, 5.4e-20
    - 23:   1, 11,  799,   21,  2,     8,  2,    988, 4.7e-20
    # no solution starting from log norm2 = 24
```

given in `output.txt`.
