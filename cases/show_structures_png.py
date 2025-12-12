#!/usr/bin/env python
"""
For a directory with xyz files generate a webpage that displays all structures

Here we do this as a two stage process:
1. Generate PNG images for all XYZ files
2. Generate a web-page showing all images

We use JMol to generate the images. Note that occasionally JMol will hang
after writing the image. This is why the timeout is needed. Afterwards the
hanging JMol-s still need to be cleaned up.
"""

import argparse
import glob
import os
import subprocess

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

def filename_xyz2png(filename_xyz):
    """
    Replace the XYZ extension with PNG
    """
    indx = filename_xyz.index(".xyz")
    filename_png = filename_xyz[:indx]+".png"
    return filename_png

def generate_png(files):
    """
    Generate a PNG image for every XYZ file
    """
    jmol = "/Users/hubertusvandam/Documents/jmol-16.3.37/jmol.sh"
    for file_xyz in files:
        file_png = filename_xyz2png(file_xyz)
        with open("jmol_script.spt","w") as fp:
            fp.write(f"load \"{file_xyz}\"")
        command = [ jmol, "-ions", "jmol_script.spt", "-w", f"PNG:{file_png}" ]
        try:
            subprocess.run(command,timeout=5)
        except subprocess.TimeoutExpired:
            print("Time out expired but I don't care")

def write_html(files_xyz):
    """
    Write an html file visualizing every xyz file with jsmol
    """
    with open("index.html","w") as fp_html:
        fp_html.write("<!DOCTYPE HTML>\n")
        fp_html.write("<HTML>\n")
        fp_html.write("<HEAD>\n")
        fp_html.write("</HEAD>\n")
        fp_html.write("<BODY>\n")
        fp_html.write("<TABLE>\n")
        for struct in files_xyz:
            file_png = filename_xyz2png(struct)
            write_row(fp_html,file_png)
        fp_html.write("</TABLE>\n")
        fp_html.write("</BODY>\n")
        fp_html.write("</HTML>\n")

def write_row(fp,file_png):
    """
    Add a single row to the table showing one structure
    """
    fp.write("<TR><TD>")
    fp.write(file_png)
    fp.write("</TD><TD>")
    line=f"<img src=\"{file_png}\" alt=\"{file_png}\">"
    fp.write(line)
    fp.write("</TD></TR>\n")

if __name__ == "__main__":
    args = commandline()
    path = args.path_xyz
    files = find_xyz_files(path)
    generate_png(files)
    write_html(files)
