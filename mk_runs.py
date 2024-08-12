#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs


project="2023-S1-UM-8"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["NGC4388+vicinity"] = [ 109948, 109949, 109953, 109954, 109960, 109961,    # 8-may
                           110036, 110037,]                                   # 26-may

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}

pars1["NGC4388+vicinity"] = "bank=0 dv=250 dw=400 b_order=1 otf_cal=1"        # only 1 bank

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}

pars2["NGC4388+vicinity"] = "pix_list=-13"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
    print("NOTE BUG: run2a and run2b both need an extra 'oid=0 bank=0'")
