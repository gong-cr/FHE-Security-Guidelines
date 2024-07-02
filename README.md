## Prerequisites
- [SageMath](https://www.sagemath.org/)

## How to Use
```bash
git clone --recursive https://github.com/gong-cr/FHE-Security-Guidelines
cd FHE-Security-Guidelines
```

For generating the table of maximum log Q, run the script:
```bash
sh max_logQ_tables.sh
```

For example,
```bash
sage max_logQ_tables.py 128 0
```

Here, 128 is the security threshold, and 0 is the security margin. The script outputts the maximum log Q that achieves the security target as 128 + 0.

To test different parameters, edit in [max_logQ_tables.py](max_logQ_tables.py).