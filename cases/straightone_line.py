#!/usr/bin/env python
"""
Extract data on the Straight-One line

The straight-one line is the line where $d^b = 1$ and $0 \\le d^a \\le 1$ and
$d_{ij} = d^a$.

This script scans a data set and outputs all the points that are on the
one-straight line. All other points are ignored.
"""
import argparse
from math import sqrt

def commandline():
    parser = argparse.ArgumentParser(
             prog="Straight-One line",
             description="Extract points in Straight-One space from a data set. Classify the points as either points on the Straight-One line or not.",
             epilog="DON'T PANIC")
    parser.add_argument("input_data",help="The file with the data set to be analyzed")
    parser.add_argument("--so-line",help="The file for the points on the Straight-One line")
    return parser.parse_args()

def classify_so(input_file,so_file):
    """
    Classify data into Straight-One and not Straight-One points
    """
    with open(input_file,"r") as fp_in, open(so_file,"w") as fp_so:
        for line in fp_in:
            words = line.split()
            occ_a = float(words[0])
            occ_b = float(words[1])
            occ_ab = float(words[2])
            ii = int(words[4])
            jj = int(words[5])
            if abs(occ_b-1.0) < 1.0e-3:
                if abs(occ_a-occ_ab) < 1.0e-3:
                    if abs(occ_a-occ_b) < 1.0e-3:
                        if jj < ii:
                            fp_so.write(line)
                    else:
                        fp_so.write(line)

if __name__ == "__main__":
    args = commandline()
    input_file = args.input_data
    if args.so_line is None:
        index = input_file.find(".dat")
        so_file = input_file[0:index]+"_so.dat"
    else:
        so_file = args.so_line
    classify_so(input_file,so_file)

