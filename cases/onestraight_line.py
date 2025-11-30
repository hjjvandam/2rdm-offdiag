#!/usr/bin/env python
"""
Extract data on the One-Straight line

The one-straight line is the line where $d^a = 1$ and $0 \\le d^b \\le 1$ and
$d_{ij} = d^b$.

This script scans a data set and outputs all the points that are on the
one-straight line. All other points are ignored.
"""
import argparse
from math import sqrt

def commandline():
    parser = argparse.ArgumentParser(
             prog="One_Straight_line",
             description="Extract points in One-Straight space from a data set. Classify the points as either points on the One-Straight line or not.",
             epilog="DON'T PANIC")
    parser.add_argument("input_data",help="The file with the data set to be analyzed")
    parser.add_argument("--os-line",help="The file for the points on the One-Straight line")
    return parser.parse_args()

def classify_os(input_file,os_file):
    """
    Classify data into One-Straight and not One-Straight points
    """
    with open(input_file,"r") as fp_in, open(os_file,"w") as fp_os:
        for line in fp_in:
            words = line.split()
            occ_a = float(words[0])
            occ_b = float(words[1])
            occ_ab = float(words[2])
            ii = int(words[4])
            jj = int(words[5])
            if abs(occ_a-1.0) < 1.0e-3:
                if abs(occ_b-occ_ab) < 1.0e-3:
                    if abs(occ_a-occ_b) < 1.0e-3:
                        if jj > ii:
                            fp_os.write(line)
                    else:
                        fp_os.write(line)

if __name__ == "__main__":
    args = commandline()
    input_file = args.input_data
    if args.os_line is None:
        index = input_file.find(".dat")
        os_file = input_file[0:index]+"_os.dat"
    else:
        os_file = args.os_line
    classify_os(input_file,os_file)

