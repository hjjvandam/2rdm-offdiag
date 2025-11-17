#!/usr/bin/env python
"""
Find all common xyz files in two files
"""
import argparse

def commandline():
    parser = argparse.ArgumentParser(
             prog="Common XYZ",
             description="Extracts common xyz structures from two files",
             epilog="DON'T PANIC")
    parser.add_argument("data_in1",help="The file with the first data set")
    parser.add_argument("data_in2",help="The file with the second data set")
    parser.add_argument("data_out",help="The for the common structures")
    return parser.parse_args()

def find_common(file1,file2,fileo):
    set1 = set()
    set2 = set()
    with open(file1,"r") as fp:
        for line in fp:
            words = line.split()
            set1.add(words[8])
    with open(file2,"r") as fp:
        for line in fp:
            words = line.split()
            set2.add(words[8])
    seto = set1 & set2
    olist = sorted(seto)
    with open(fileo,"w") as fp:
        for item in olist:
            # This format ensures we can further process the data
            fp.write(f"x.xxx x.xxx x.xxx # x x xxxx xxxx {item}")

if __name__ == "__main__":
    args = commandline()
    f_in1 = args.data_in1
    f_in2 = args.data_in2
    f_out = args.data_out
    find_common(f_in1,f_in2,f_out)
