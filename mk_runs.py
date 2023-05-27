#! /usr/bin/env python
#

import os
import sys


from lmtoy import runs


project="2023-S1-UM-8"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["NGC4388+vicinity"] = [ 109948, 109949, 109953, 109954, 109960, 109961,    8-may
                           110036, 110036,]                                  26-may

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}

pars1["NGC4388+vicinity"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}

pars2["NGC4388+vicinity"] = "pix_list=-13"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2)
