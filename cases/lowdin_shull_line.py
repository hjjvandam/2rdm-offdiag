#!/usr/bin/env python
"""
Extract data on the Lowdin-Shull line

The paper by Lowdin and Shull [1] discusses density matrices of two electron systems.
One key result is that some 2-electron density matrix elements can be expressed
in terms of the 1-electron density matrix occupation numbers as (see [1] equation 48)

:math:`d_{ij} = \\sqrt{d^a_i d^b_j}, i = j`

In plots of the diagonal elements of the 2-electron density matrix these data points
show up as a straight line from $d^a = 0, d^b = 0, d_{ij} = 0$ to
$d^a = 1, d^b = 1, d_{ij} = 1$. I'll refer to points along this line as the
Lowdin-Shull line.

This script looks at alpha-beta electron data sets and extracts points in the
Lowdin-Shull space, which we define as elements $d_{ij}$ where $i=j$.
We output two sets of points. Those are points that either on the Lowdin-Shull
line, or points in the Lowdin-Shull space but that are not on the Lowdin-Shull line.

[1] Lowdin and Shull. Phys. Rev. 101 (1956), 1730-1739. DOI: https://doi.org/10.1103/PhysRev.101.1730
"""
import argparse
from math import sqrt

def commandline():
    parser = argparse.ArgumentParser(
             prog="Lowdin_Shull_line",
             description="Extract points in Lowdin-Shull space from a data set. Classify the points as either points on the Lowdin-Shull line and other points. Write out both sets of points.",
             epilog="DON'T PANIC")
    parser.add_argument("input_data",help="The file with the data set to be analyzed")
    parser.add_argument("--ls-line",help="The file for the points on the Lowdin-Shull line")
    parser.add_argument("--not-ls-line",help="The file for the points not on the Lowdin-Shull line")
    return parser.parse_args()

def classify_ls(input_file,ls_file,nls_file):
    """
    Classify data into Lowdin-Shull and not Lowdin-Shull points
    """
    with open(input_file,"r") as fp_in, open(ls_file,"w") as fp_ls, open(nls_file,"w") as fp_nls:
        for line in fp_in:
            words = line.split()
            occ_a = float(words[0])
            occ_b = float(words[1])
            occ_ab = float(words[2])
            ii = int(words[4])
            jj = int(words[5])
            if occ_a > 1.0e-5 and occ_b > 1.0e-5:
                if abs(occ_a-occ_b) < 0.5e-3*(occ_a+occ_b):
                    if abs(sqrt(occ_a*occ_b)-occ_ab) < 0.5e-2*(sqrt(occ_a*occ_b)+occ_ab):
                        if ii == jj:
                            fp_ls.write(line)
                        else:
                            fp_nls.write(line)
                    else:
                        fp_nls.write(line)
            #else:
            # The point is not in the Lowdin-Shull space

if __name__ == "__main__":
    args = commandline()
    input_file = args.input_data
    if args.ls_line is None:
        index = input_file.find(".dat")
        ls_file = input_file[0:index]+"_ls.dat"
    else:
        ls_file = args.ls_line
    if args.not_ls_line is None:
        index = input_file.find(".dat")
        nls_file = input_file[0:index]+"_nls.dat"
    else:
        nls_file = args.not_ls_line
    classify_ls(input_file,ls_file,nls_file)

