#!/usr/bin/env python
"""
Group the sums per line by case

With the 2RDM certain traces have to be maintained. Here we have split the
2RDM elements by lines. When combining the traces across all lines the
overall trace has to be recovered. At the same time grouping the results
by case enables to investigate how the distribution across lines changes
between different cases.

This script takes an number files with traces and collects the traces by
case. It also computes the overall trace. Then it writes the resulting
table as a CSV file.
"""
import argparse
import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)

def commandline():
    parser = argparse.ArgumentParser(
             prog="Summarize traces",
             description="Summarize traces by grouping them by case",
             epilog="DON'T PANIC")
    parser.add_argument("--ls",
                        help="file with traces of the Lowdin-Shull line by case",
                        default=None)
    parser.add_argument("--hs",
                        help="file with traces of the half-straight line by case",
                        default=None)
    parser.add_argument("--sh",
                        help="file with traces of the straight-half line by case",
                        default=None)
    parser.add_argument("--hh",
                        help="file with traces of the half-half line by case",
                        default=None)
    parser.add_argument("--os",
                        help="file with traces of the one-straight line by case",
                        default=None)
    parser.add_argument("--so",
                        help="file with traces of the straight-one line by case",
                        default=None)
    parser.add_argument("--en",
                        help="file with traces of the eye-negative line by case",
                        default=None)
    parser.add_argument("--ep",
                        help="file with traces of the eye-positive line by case",
                        default=None)
    return parser.parse_args()

def read_file(filein,name):
    """
    Read a file with traces and return a single column Panda data frame

    The returned Panda data frame contains a single column. The name of the column
    is the value of `name`. The rows are labeled with the case names.
    """
    cases = []
    values = []
    with open(filein,"r") as fp:
        for line in fp:
            words = line.split()
            value = float(words[8])
            case  = words[10]
            cases.append(case)
            values.append(value)
    dataframe = pd.DataFrame({"case": cases, name: values})
    return dataframe

def gather_data(ls,sh,hs,hh,so,os,en,ep):
    """
    Load all the files and compose a combined data frame

    For the eye lines we do something special. If both positive and
    negative lines are provided we combine both as ey = en - ep, and
    we'll add ey.
    """
    dataframe = pd.DataFrame(columns=["case"])
    if not ls is None:
        ls_pd = read_file(ls,"ls")
        dataframe = pd.merge(dataframe,ls_pd,how="outer", on="case")
    if not sh is None:
        sh_pd = read_file(sh,"sh")
        dataframe = pd.merge(dataframe,sh_pd,how="outer", on="case")
    if not hs is None:
        hs_pd = read_file(hs,"hs")
        dataframe = pd.merge(dataframe,hs_pd,how="outer", on="case")
    if not hh is None:
        hh_pd = read_file(hh,"hh")
        dataframe = pd.merge(dataframe,hh_pd,how="outer", on="case")
    if not so is None:
        so_pd = read_file(so,"so")
        dataframe = pd.merge(dataframe,so_pd,how="outer", on="case")
    if not os is None:
        os_pd = read_file(os,"os")
        dataframe = pd.merge(dataframe,os_pd,how="outer", on="case")
    if (not en is None) and (not ep is None):
        en_pd = read_file(en,"en")
        ep_pd = read_file(ep,"ep")
        et_pd = pd.merge(en,ep,how="outer",on="case")
        et_pd["en"] = et_pd["en"].apply(lambda x: 0.0 if pd.isna(x) else x)
        et_pd["ep"] = et_pd["ep"].apply(lambda x: 0.0 if pd.isna(x) else x)
        #ey_pd["ey"] = et_pd.apply(lambda x: et_pd["en"]-et_pd["ep"])
        ey_pd["ey"] = et_pd["en"]-et_pd["ep"]
        dataframe = pd.merge(dataframe,ey_pd,how="outer", on="case")
    elif (not en is None) and (ep is None):
        ey_pd = read_file(en,"ey")
        dataframe = pd.merge(dataframe,ey_pd,how="outer", on="case")
    elif (en is None) and (not ep is None):
        ey_pd = read_file(ep,"ey")
        ey_pd["ey"] = ey_pd.apply(lambda x: -x)
        dataframe = pd.merge(dataframe,ey_pd,how="outer", on="case")
    if not ls is None:
        dataframe["ls"] = dataframe["ls"].apply(lambda x: 0.0 if pd.isna(x) else x)
    if not hs is None:
        dataframe["hs"] = dataframe["hs"].apply(lambda x: 0.0 if pd.isna(x) else x)
    if not sh is None:
        dataframe["sh"] = dataframe["sh"].apply(lambda x: 0.0 if pd.isna(x) else x)
    if not hh is None:
        dataframe["hh"] = dataframe["hh"].apply(lambda x: 0.0 if pd.isna(x) else x)
    if not os is None:
        dataframe["os"] = dataframe["os"].apply(lambda x: 0.0 if pd.isna(x) else x)
    if not so is None:
        dataframe["so"] = dataframe["so"].apply(lambda x: 0.0 if pd.isna(x) else x)
    if (not en is None) or (not ep is None):
        dataframe["ey"] = dataframe["ey"].apply(lambda x: 0.0 if pd.isna(x) else x)
    dataframe["Total"] = dataframe.sum(numeric_only=True,axis=1)
    return dataframe

if __name__ == "__main__":
    args = commandline()
    ls = args.ls
    hs = args.hs
    sh = args.sh
    hh = args.hh
    os = args.os
    so = args.so
    en = args.en
    ep = args.ep
    data = gather_data(ls,sh,hs,hh,so,os,en,ep)
    print(data)
