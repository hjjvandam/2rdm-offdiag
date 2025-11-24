#!/usr/bin/env python
"""
Extract data on the Half-Half line

The half-half line is the line where $d^a = d^b = 1/2$.

This script scans a data set and outputs all the points that are on the
half-half line. All other points are ignored.
"""
import argparse
from math import sqrt

def commandline():
    parser = argparse.ArgumentParser(
             prog="Half-Half line",
             description="Extract points in Half-Half space from a data set. Classify the points as either points on the Half-Half line or not.",
             epilog="DON'T PANIC")
    parser.add_argument("input_data",help="The file with the data set to be analyzed")
    parser.add_argument("--hh-line",help="The file for the points on the Half-Half line")
    return parser.parse_args()

def classify_hh(input_file,hh_file):
    """
    Classify data into Half-Half and not Half-Half points
    """
    with open(input_file,"r") as fp_in, open(hh_file,"w") as fp_hh:
        for line in fp_in:
            words = line.split()
            occ_a = float(words[0])
            occ_b = float(words[1])
            occ_ab = float(words[2])
            ii = int(words[4])
            jj = int(words[5])
            if abs(occ_a-0.5) < 1.0e-3:
                if abs(occ_b-0.5) < 1.0e-3:
                    if (abs(occ_ab-0.50) > 1.0e-3 and
                        abs(occ_ab-0.25) > 1.0e-3 and
                        abs(occ_ab     ) > 1.0e-3 and
                        abs(occ_ab+0.50) > 1.0e-3):
                        fp_hh.write(line)

if __name__ == "__main__":
    args = commandline()
    input_file = args.input_data
    if args.hh_line is None:
        index = input_file.find(".dat")
        hh_file = input_file[0:index]+"_hh.dat"
    else:
        hh_file = args.hh_line
    classify_hh(input_file,hh_file)

