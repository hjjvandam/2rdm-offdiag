#!/usr/bin/env python
"""
For a directory with xyz files generate a webpage that displays all structures
"""

import argparse
import glob
import os

def commandline():
    parser = argparse.ArgumentParser(
             prog="Show structures",
             description="Generate a web-page to display a collection of xyz structures",
             epilog="DON'T PANIC")
    parser.add_argument("path_xyz",help="the directory where xyz files reside")
    return parser.parse_args()

def find_xyz_files(path):
    """
    Given the directory find all the xyz files within and return their names in an ordered list
    """
    os.chdir(path)
    files = []
    for file in glob.glob("*.xyz"):
        files.append(file)
    files.sort()
    return files

def write_html(files_xyz):
    """
    Write an html file visualizing every xyz file with jsmol
    """
    with open("index.html","w") as fp_html:
        fp_html.write("<!DOCTYPE HTML>\n")
        fp_html.write("<HTML>\n")
        fp_html.write("<HEAD>\n")
        fp_html.write("  <SCRIPT src=\"../jmol/jsmol/JSmol.min.js\"></script>\n")
        fp_html.write("  <SCRIPT src=\"../jmol/jsmol/js/Jmol2.js\"></script>\n")
        fp_html.write("  <SCRIPT> jmolInitialize(\"../jmol/jsmol\");</script>\n")
        fp_html.write("</HEAD>\n")
        fp_html.write("<BODY>\n")
        fp_html.write("<TABLE>\n")
        for struct in files_xyz:
            write_row(fp_html,struct)
        fp_html.write("</TABLE>\n")
        fp_html.write("</BODY>\n")
        fp_html.write("</HTML>\n")

def write_row(fp,file_xyz):
    """
    Add a single row to the table showing one structure
    """
    fp.write("<TR><TD>")
    fp.write(file_xyz)
    fp.write("</TD><TD>")
    line="<script>jmolApplet(200,\"load "+file_xyz+"\",\"0\")</script>"
    fp.write(line)
    fp.write("</TD></TR>\n")

if __name__ == "__main__":
    args = commandline()
    path = args.path_xyz
    files = find_xyz_files(path)
    write_html(files)
