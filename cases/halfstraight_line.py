#!/usr/bin/env python
"""
Extract data on the Half-Straight line

The half-straight line is the line where $d^a = 1/2$ and $0 \\le d^b \\le 1$ and
$d_{ij} = d^a d^b$.

This script scans a data set and outputs all the points that are on the
half-straight line. All other points are ignored.
"""
import argparse
from math import sqrt

def commandline():
    parser = argparse.ArgumentParser(
             prog="Half-Straight_line",
             description="Extract points in Half-Straight space from a data set. Classify the points as either points on the Half-Straight line or not.",
             epilog="DON'T PANIC")
    parser.add_argument("input_data",help="The file with the data set to be analyzed")
    parser.add_argument("--hs-line",help="The file for the points on the Half-Straight line")
    return parser.parse_args()

def classify_hs(input_file,hs_file):
    """
    Classify data into Half-Straight and not Half-Straight points
    """
    with open(input_file,"r") as fp_in, open(hs_file,"w") as fp_hs:
        for line in fp_in:
            words = line.split()
            occ_a = float(words[0])
            occ_b = float(words[1])
            occ_ab = float(words[2])
            ii = int(words[4])
            jj = int(words[5])
            if abs(occ_a-0.5) < 1.0e-3:
                if abs(occ_a*occ_b-occ_ab) < 1.0e-3:
                    if abs(occ_a-occ_b) < 1.0e-3:
                        if jj > ii:
                            fp_hs.write(line)
                    else:
                        fp_hs.write(line)

if __name__ == "__main__":
    args = commandline()
    input_file = args.input_data
    if args.hs_line is None:
        index = input_file.find(".dat")
        hs_file = input_file[0:index]+"_hs.dat"
    else:
        hs_file = args.hs_line
    classify_hs(input_file,hs_file)
