#!/usr/bin/env python3
"""Check every solution of the repository against its instance.

    check_all.py

For each solutions/<class>/<name>.sol, runs check_sol on
instances/<class>/<name>.dat. Exit status 0 only if every file is OK.
"""
import glob
import os
import sys

from check_sol import main as check

here = os.path.dirname(os.path.abspath(__file__))
bad = total = 0
for sol in sorted(glob.glob(os.path.join(here, "solutions", "*", "*.sol"))):
    cls = os.path.basename(os.path.dirname(sol))
    name = os.path.splitext(os.path.basename(sol))[0]
    dat = os.path.join(here, "instances", cls, name + ".dat")
    verdict = check(dat, sol) if os.path.exists(dat) else "instance file missing"
    total += 1
    bad += verdict != "OK"
    print("%s/%s: %s" % (cls, name, verdict))
print("%d of %d solutions OK" % (total - bad, total))
sys.exit(1 if bad else 0)
