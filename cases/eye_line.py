#!/usr/bin/env python
"""
Extract data on the Eye lines

The off-diagonal elements of the 2RDM tend to form an "eye" along the line
x = 1-y. There is a postive and a negative arch to this "eye". The elements
on the negative arch lead to a lowering of the total energy, the elements of
the positve arch drive the energy up.

This script looks for points in the eye space (i.e. on the x = 1-y line).
Then the points are separated into positive and negative points, subsequently
the points are separated into points on the corresponding eye line and points
that are between the eye line and zero.

The four sets are written out to their own files.
"""
import argparse
from math import sqrt

def commandline():
    parser = argparse.ArgumentParser(
             prog="Eye_line",
             description="Extract points in Eye space from a data set. Classify the points as either positive or negative points, and either on or off the eye line. Write out all four sets of points.",
             epilog="DON'T PANIC")
    parser.add_argument("input_data",help="The file with the data set to be analyzed")
    parser.add_argument("--ep-line",help="The file for the points on the positive eye line")
    parser.add_argument("--not-ep-line",help="The file for the positive points not on the eye line")
    parser.add_argument("--en-line",help="The file for the points on the negative eye line")
    parser.add_argument("--not-en-line",help="The file for the negative points not on the eye line")
    return parser.parse_args()

def eye(x,y):
    """
    The correlation function.
    """
    res = sqrt(sqrt(x*(1.0-x)*y*(1.0-y)))
    return res

def classify_eye(input_file,ep_file,nep_file,en_file,nen_file):
    """
    Classify data into various eye spaces
    """
    with open(input_file,"r") as fp_in, open(ep_file,"w") as fp_ep, open(nep_file,"w") as fp_nep, open(en_file,"w") as fp_en, open(nen_file,"w") as fp_nen:
        for line in fp_in:
            words = line.split()
            occ_a = float(words[0])
            occ_b = float(words[1])
            occ_ab = float(words[2])
            ii = int(words[4])
            jj = int(words[5])
            if abs(occ_a-(1.0-occ_b)) < 1.0e-3: # occ_a + occ_b == 1
                if occ_ab > 1.0e-4:
                    if abs(eye(occ_a,occ_b)-occ_ab) < 5.0e-3*(eye(occ_a,occ_b)+occ_ab):
                        fp_ep.write(line)
                    else:
                        fp_nep.write(line)
                elif occ_ab < 1.0e-4:
                    if abs(eye(occ_a,occ_b)+occ_ab) < 5.0e-3*(eye(occ_a,occ_b)-occ_ab):
                        fp_en.write(line)
                    else:
                        fp_nen.write(line)
            #else:
            # The point is not in the Eye space

if __name__ == "__main__":
    args = commandline()
    input_file = args.input_data
    if args.ep_line is None:
        index = input_file.find(".dat")
        ep_file = input_file[0:index]+"_ep.dat"
    else:
        ep_file = args.ep_line
    if args.not_ep_line is None:
        index = input_file.find(".dat")
        nep_file = input_file[0:index]+"_nep.dat"
    else:
        nep_file = args.not_ep_line
    if args.en_line is None:
        index = input_file.find(".dat")
        en_file = input_file[0:index]+"_en.dat"
    else:
        en_file = args.en_line
    if args.not_en_line is None:
        index = input_file.find(".dat")
        nen_file = input_file[0:index]+"_nen.dat"
    else:
        nen_file = args.not_en_line
    classify_eye(input_file,ep_file,nep_file,en_file,nen_file)

