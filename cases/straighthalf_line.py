#!/usr/bin/env python
"""
Extract data on the Straight-Half line

The straight-half line is the line where $d^b = 1/2$ and $0 \\le d^a \\le 1$ and
$d_{ij} = d^a d^b$.

This script scans a data set and outputs all the points that are on the
straight-half line. All other points are ignored.
"""
import argparse
from math import sqrt

def commandline():
    parser = argparse.ArgumentParser(
             prog="Straight-Half line",
             description="Extract points in Straight-Half space from a data set. Classify the points as either points on the Straight-Half line or not.",
             epilog="DON'T PANIC")
    parser.add_argument("input_data",help="The file with the data set to be analyzed")
    parser.add_argument("--sh-line",help="The file for the points on the Straight-Half line")
    return parser.parse_args()

def classify_sh(input_file,sh_file):
    """
    Classify data into Straight-Half and not Straight-Half points
    """
    with open(input_file,"r") as fp_in, open(sh_file,"w") as fp_sh:
        for line in fp_in:
            words = line.split()
            occ_a = float(words[0])
            occ_b = float(words[1])
            occ_ab = float(words[2])
            ii = int(words[4])
            jj = int(words[5])
            if abs(occ_b-0.5) < 1.0e-3:
                if abs(occ_a*occ_b-occ_ab) < 1.0e-3:
                    if abs(occ_a-occ_b) < 1.0e-3:
                        if jj < ii:
                            fp_sh.write(line)
                    else:
                        fp_sh.write(line)

if __name__ == "__main__":
    args = commandline()
    input_file = args.input_data
    if args.sh_line is None:
        index = input_file.find(".dat")
        sh_file = input_file[0:index]+"_sh.dat"
    else:
        sh_file = args.sh_line
    classify_sh(input_file,sh_file)
