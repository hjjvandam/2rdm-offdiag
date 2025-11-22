#!/usr/bin/env python
"""
Sum RDM elements

We sum both the 1-electron occupation numbers as well as the
2 RDM elements for a data file.
"""
import argparse

def commandline():
    parser = argparse.ArgumentParser(
             prog="Sum RDM",
             description="Sum the RDM elements",
             epilog="DON'T PANIC")
    parser.add_argument("data_in",help="The file with the data set")
    return parser.parse_args()

def compute_sums(filein):
    occa = 0.0
    occb = 0.0
    rdm2p = 0.0
    rdm2m = 0.0
    rdm2t = 0.0
    nlines = 0
    with open(filein,"r") as fp:
        for line in fp:
            nlines += 1
            words = line.split()
            occa += float(words[0])
            occb += float(words[1])
            rdm2 = float(words[2])
            if rdm2 > 0.0:
                rdm2p += rdm2
            else:
                rdm2m += rdm2
    print(f"occa {occa}   occb {occb}   rdm2 {rdm2p} {rdm2m} {rdm2p-rdm2m}")

if __name__ == "__main__":
    args = commandline()
    f_in = args.data_in
    compute_sums(f_in)
