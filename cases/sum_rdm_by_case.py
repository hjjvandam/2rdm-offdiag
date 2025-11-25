#!/usr/bin/env python
"""
Sum RDM elements by case

We sum RDM elements by case. The summation by case is a bit unusual.
We collect the unique orbital numbers and occupation numbers for
both occ_a and occ_b.
In addition we sum the 2RDM elements.
Then we print a report by case.
"""
import argparse

def commandline():
    parser = argparse.ArgumentParser(
             prog="Sum RDM by Case",
             description="Sum the RDM elements by Case",
             epilog="DON'T PANIC")
    parser.add_argument("data_in",help="The file with the data set")
    return parser.parse_args()

def compute_sums(filein):
    occa = 0.0
    occb = 0.0
    rdm2p = 0.0
    rdm2m = 0.0
    rdm2t = 0.0
    nlines_tot = 0
    case = ""
    orba = set()
    orbb = set()
    with open(filein,"r") as fp:
        for line in fp:
            words = line.split()
            if words[8] != case:
                if nlines_tot != 0:
                    print(f"lines {nlines_tot:6d} {nlines_case:4d}  occa {occa_case:10.3f}   occb {occb_case:10.3f}   rdm2 {rdm2_case:10.3f}   case {case}")
                occa_case = 0.0
                occb_case = 0.0
                rdm2_case = 0.0
                orba_set  = set()
                orbb_set  = set()
                case = words[8]
                nlines_case = 0
            nlines_tot += 1
            nlines_case += 1
            occa = float(words[0])
            occb = float(words[1])
            rdm2 = abs(float(words[2]))
            orba = int(words[4])
            orbb = int(words[5])
            if not orba in orba_set:
                orba_set.add(orba)
                occa_case += occa
            if not orbb in orbb_set:
                orbb_set.add(orbb)
                occb_case += occb
            rdm2_case += rdm2
        print(f"lines {nlines_tot:6d} {nlines_case:4d}  occa {occa_case:10.3f}   occb {occb_case:10.3f}   rdm2 {rdm2_case:10.3f}   case {case}")

if __name__ == "__main__":
    args = commandline()
    f_in = args.data_in
    compute_sums(f_in)
