#!/usr/bin/env python3
"""Independent check of a solution file against its instance.

    check_sol.py <instance.dat> <solution.sol>

Reads the instance in the format of the cb_benchmark files (n, m, then the n
profits, the m capacities, then m rows of n weights; anything after that is
ignored) and the solution file (line 1: n values 0/1, line 2:
the claimed objective). Recomputes the objective and every constraint with
integer arithmetic and prints OK or a reason. Exit status 0 only on OK.
"""
import sys

def main(dat, sol):
    nums = [int(float(t)) for t in open(dat).read().split()]
    n, m = nums[0], nums[1]
    pos = 2
    p = nums[pos:pos + n]; pos += n
    b = nums[pos:pos + m]; pos += m
    a = [nums[pos + i * n:pos + (i + 1) * n] for i in range(m)]
    lines = [l for l in open(sol).read().split('\n') if l.strip()]
    x = [int(t) for t in lines[0].split()]
    claimed = int(lines[1].split()[-1])
    if len(x) != n or any(v not in (0, 1) for v in x):
        return "bad vector: %d values, expected %d binaries" % (len(x), n)
    obj = sum(pj * xj for pj, xj in zip(p, x))
    if obj != claimed:
        return "objective %d != claimed %d" % (obj, claimed)
    for i in range(m):
        load = sum(aij * xj for aij, xj in zip(a[i], x))
        if load > b[i]:
            return "constraint %d violated: %d > %d" % (i, load, b[i])
    return "OK"

if __name__ == "__main__":
    verdict = main(sys.argv[1], sys.argv[2])
    print("%s: %s" % (sys.argv[2], verdict))
    sys.exit(0 if verdict == "OK" else 1)
