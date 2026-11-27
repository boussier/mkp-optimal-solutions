# Optimal solutions of 0–1 multidimensional knapsack instances

Optimal solutions of benchmark instances of the 0–1 multidimensional knapsack
problem (MKP), with a small independent checker.

The repository covers 150 instances of the [OR-Library](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/mknapinfo.html)
(Chu and Beasley [1]), in five classes of thirty instances each. A class
`cbM.N` has `M` constraints and `N` variables.

| Class | Constraints | Variables | OR-Library file | Optimality proofs |
|---|---|---|---|---|
| `cb5.250` | 5 | 250 | `mknapcb2.txt` | published in [4] |
| `cb5.500` | 5 | 500 | `mknapcb3.txt` | published in [4] |
| `cb10.250` | 10 | 250 | `mknapcb5.txt` | published in [4] |
| `cb10.500` | 10 | 500 | `mknapcb6.txt` | published in [2] |
| `cb30.250` | 30 | 250 | `mknapcb8.txt` | seven in [2], twenty-three in [3] |

In the class `cb30.250`, seven instances were solved to proven optimality in
2010 [2]. The other twenty-three had been open since 1998; they were closed in
2026 by a parallel resolution search [3]. Each optimal value equals the best
value previously reported in the literature: what was missing was the proof.

For the four other classes the optimal values were already known. The
solutions given here were computed again in 2026 with our resolution search
solver, and each run ended with a proof of optimality. The 120 values equal those
published in [5]; for the classes `cb10.250`, `cb5.500` and `cb10.500` they
also equal those of [2].

The file `optimal_values.csv` lists the 150 instances with their optimal
value.

## Contents

    solutions/<class>/    one optimal solution per instance (.sol)
    instances/<class>/    the instances, one file each (.dat)
    optimal_values.csv    the optimal value of every instance
    check_sol.py          checks one solution against its instance
    check_all.py          checks every solution of the repository

## Checking the solutions

Python 3, no dependency.

    python3 check_all.py
    python3 check_sol.py instances/cb30.250/cb30.250_8.dat solutions/cb30.250/cb30.250_8.sol

The checker reads the instance, recomputes the objective value and the
left-hand side of every constraint in integer arithmetic, and compares them
with the claimed value and the capacities. `check_all.py` also compares each
value with the one listed in `optimal_values.csv`.

**What the checker establishes.** It shows that each solution is feasible and
has the stated value. It does not show that the value is optimal: optimality
rests on the exhaustive searches described in the papers cited above, and a feasible solution is
only a certificate of the lower bound.

## File formats

Instance file (`.dat`), whitespace-separated integers:

    n m
    c_1 ... c_n                  profits
    b_1 ... b_m                  capacities
    a_11 ... a_1n                weights, one row per constraint
    ...
    a_m1 ... a_mn

The problem is: maximise `sum_j c_j x_j` subject to `sum_j a_ij x_j <= b_i` for
`i = 1..m`, with `x_j` in `{0, 1}`. The data are those of the files of the
[OR-Library](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/mknapinfo.html) named in the table above; only the layout differs
(one file per instance, capacities before the weights). Instance `cbM.N_k` is
the instance number `k` of its OR-Library file, counted from 0.

Solution file (`.sol`):

    x_1 ... x_n                  values 0 or 1, in the order of the instance file
    value                        objective value of this solution

## The thirty 30 × 250 instances

The tightness ratio is the capacity of each constraint divided by the sum of
its weights.

| Instance | Tightness | Optimal value | Optimality proof |
|---|---|---|---|
| `cb30.250_0` | 0.25 | 56842 | first proof, this work |
| `cb30.250_1` | 0.25 | 58520 | first proof, this work |
| `cb30.250_2` | 0.25 | 56614 | first proof, this work |
| `cb30.250_3` | 0.25 | 56930 | first proof, this work |
| `cb30.250_4` | 0.25 | 56629 | first proof, this work |
| `cb30.250_5` | 0.25 | 57205 | first proof, this work |
| `cb30.250_6` | 0.25 | 56357 | first proof, this work |
| `cb30.250_7` | 0.25 | 56457 | first proof, this work |
| `cb30.250_8` | 0.25 | 57474 | first proof, this work |
| `cb30.250_9` | 0.25 | 56447 | first proof, this work |
| `cb30.250_10` | 0.5 | 107770 | first proof, this work |
| `cb30.250_11` | 0.5 | 108392 | first proof, this work |
| `cb30.250_12` | 0.5 | 106442 | first proof, this work |
| `cb30.250_13` | 0.5 | 106876 | first proof, this work |
| `cb30.250_14` | 0.5 | 107414 | first proof, this work |
| `cb30.250_15` | 0.5 | 107271 | first proof, this work |
| `cb30.250_16` | 0.5 | 106372 | first proof, this work |
| `cb30.250_17` | 0.5 | 104032 | first proof, this work |
| `cb30.250_18` | 0.5 | 106856 | first proof, this work |
| `cb30.250_19` | 0.5 | 105780 | first proof, this work |
| `cb30.250_20` | 0.75 | 150163 | 2010 [2], proved again in this work |
| `cb30.250_21` | 0.75 | 149958 | 2010 [2], proved again in this work |
| `cb30.250_22` | 0.75 | 153007 | 2010 [2], proved again in this work |
| `cb30.250_23` | 0.75 | 153234 | 2010 [2], proved again in this work |
| `cb30.250_24` | 0.75 | 150287 | 2010 [2], proved again in this work |
| `cb30.250_25` | 0.75 | 148574 | first proof, this work |
| `cb30.250_26` | 0.75 | 147477 | 2010 [2], proved again in this work |
| `cb30.250_27` | 0.75 | 152912 | 2010 [2], proved again in this work |
| `cb30.250_28` | 0.75 | 149570 | first proof, this work |
| `cb30.250_29` | 0.75 | 149668 | first proof, this work |

## License

The checker scripts are under the MIT license (see `LICENSE`). The instance data
come from the [OR-Library](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/mknapinfo.html) of J. E. Beasley.

## References

[1] P. C. Chu and J. E. Beasley. A genetic algorithm for the multidimensional
knapsack problem. *Journal of Heuristics*, 4(1):63–86, 1998.
https://doi.org/10.1023/A:1009642405419

[2] S. Boussier, M. Vasquez, Y. Vimont, S. Hanafi and P. Michelon. A
multi-level search strategy for the 0–1 multidimensional knapsack problem.
*Discrete Applied Mathematics*, 158(2):97–109, 2010.

[3] S. Boussier, M. Vasquez, E. SanJuan and S. Gueye. Closing the 30 × 250
OR-Library instances of the 0–1 multidimensional knapsack problem by parallel
resolution search. In preparation, 2026.

[4] Y. Vimont, S. Boussier and M. Vasquez. Reduced costs propagation in an
efficient implicit enumeration for the 0–1 multidimensional knapsack problem.
*Journal of Combinatorial Optimization*, 15(2):165–178, 2008.
https://doi.org/10.1007/s10878-007-9074-4

[5] R. Mansini and M. G. Speranza. CORAL: an exact algorithm for the
multidimensional knapsack problem. *INFORMS Journal on Computing*,
24(3):399–415, 2012. https://doi.org/10.1287/ijoc.1110.0460

## How to cite

Please cite reference [3]. This section will be updated when the paper is
available.
