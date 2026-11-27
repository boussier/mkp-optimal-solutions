#!/usr/bin/env python3
"""Check every solution of the repository against its instance.

    check_all.py

For each solutions/<class>/<name>.sol, runs check_sol on
instances/<class>/<name>.dat, then compares the value of the solution with the
optimal value listed in optimal_values.csv. Exit status 0 only if every file
is OK and every listed instance has a solution.
"""
import csv
import glob
import os
import sys

from check_sol import main as check

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "optimal_values.csv")) as f:
    listed = {row["instance"]: int(row["optimal_value"]) for row in csv.DictReader(f)}
bad = total = 0
seen = set()
for sol in sorted(glob.glob(os.path.join(here, "solutions", "*", "*.sol"))):
    cls = os.path.basename(os.path.dirname(sol))
    name = os.path.splitext(os.path.basename(sol))[0]
    dat = os.path.join(here, "instances", cls, name + ".dat")
    verdict = check(dat, sol) if os.path.exists(dat) else "instance file missing"
    if verdict == "OK":
        value = int(open(sol).read().split()[-1])
        if name not in listed:
            verdict = "not listed in optimal_values.csv"
        elif value != listed[name]:
            verdict = "value %d != listed optimum %d" % (value, listed[name])
    seen.add(name)
    total += 1
    bad += verdict != "OK"
    if verdict != "OK":
        print("%s/%s: %s" % (cls, name, verdict))
missing = sorted(set(listed) - seen)
for name in missing:
    print("%s: listed in optimal_values.csv, no solution file" % name)
print("%d of %d solutions OK" % (total - bad, total))
sys.exit(1 if bad or missing else 0)
