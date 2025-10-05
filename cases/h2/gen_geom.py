#!/usr/bin/env python
"""
Script to generate random structures consisting of 2 Hydrogen atoms

The first atom is placed at the origin.
The second atom is placed along the z-axis up to +5 A
"""
import random

for ii in range(200):
    z2 = random.uniform(0.0,5.0)
    with open(f"h2-{ii:04d}.xyz","w") as fp:
        fp.write("2\n\n")
        fp.write("h 0 0 0\n")
        fp.write(f"h 0 0 {z2}\n")
