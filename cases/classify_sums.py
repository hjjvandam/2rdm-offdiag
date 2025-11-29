#!/usr/bin/env python
"""
Classify sum by case elements

We have a sum_rdm_by_case script. This script calculates traces of density
matrix lines by case. Here a case is a single Full-CI calculation. Interestingly
the values of these traces seem to be quantized. I.e. they tend to be integer
but they are also not the same for every case. For example, with h2 we get
1.0 for every case, with h4 we get either 1.0 or 2.0, with h6 we get either
1.0, 2.0, or 3.0. So the answer is different dependent on the geometry and
what Full-CI state happens to have the lowest energy?

As we cannot solve the confusion right now, we can at least try to map it.
For this purpose this script reads to output from sum_rdm_by_case.py and
bins the counts and reports the number of occurances of each count.
"""
import argparse
import matplotlib.pyplot as plt
import numpy as np

def commandline():
    parser = argparse.ArgumentParser(
             prog="Classify Sums",
             description="Classify the sum of RDM elements",
             epilog="DON'T PANIC")
    parser.add_argument("data_in",help="The file with the data set (output from sum_rdm_by_case.py)")
    return parser.parse_args()

def classify_sums(filein):
    """
    We do two passes through the file:
    1. Find the maximum sums
    2. Build a histogram of values
    """
    rdm_max = 0.0
    nlines = 0
    with open(filein,"r") as fp:
        for line in fp:
            nlines += 1
            words = line.split()
            rdm2 = float(words[8])
            if rdm2 > rdm_max:
                rdm_max = rdm2
    num = int(rdm_max*100.0+2.0)
    values = np.zeros(nlines)
    ii = -1
    with open(filein,"r") as fp:
        for line in fp:
            ii += 1
            words = line.split()
            rdm2 = float(words[8])
            values[ii] = rdm2
    #print(rdm_max)
    #print(num)
    #print(values)
    histo = np.histogram(values,bins=num,range=(-0.01,rdm_max+0.02))
    #print(histo)
    return histo

def plot_histogram(histo):
    """
    Plot the histogram
    """
    counts, bins = histo
    #plt.hist(histo)
    #plt.bar(bins[:-1],counts,width=0.01)
    bincentres = [(bins[i]+bins[i+1])/2. for i in range(len(bins)-1)]
    plt.step(bincentres,counts,where='mid')
    plt.show()

def print_histogram(histo):
    """
    Print the histogram
    """
    counts, bins = histo
    bincentres = [(bins[i]+bins[i+1])/2. for i in range(len(bins)-1)]
    for ii in range(len(bins)-1):
        if counts[ii] > 0:
            print(f"{bincentres[ii]} {counts[ii]}")

if __name__ == "__main__":
    args = commandline()
    input_file = args.data_in
    histogram = classify_sums(input_file)
    print_histogram(histogram)
    plot_histogram(histogram)
