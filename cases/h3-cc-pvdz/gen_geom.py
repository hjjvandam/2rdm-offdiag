#!/usr/bin/env python
"""
Script to generate random structures consisting of 3 Hydrogen atoms

The first atom is placed at the origin.
The second atom is placed along the z-axis up to +5 A
The thrid atom is placed within -5 to +5 A from the second along the z-axis
          and from 0 to 5 A along the y-axis
"""
import random

for ii in range(1000):
    z2 = random.uniform(0.0,5.0)
    z3 = z2 + random.uniform(-5.0,5.0)
    y3 = random.uniform(0.0,5.0)
    with open(f"h3-{ii:04d}.xyz","w") as fp:
        fp.write("3\n\n")
        fp.write("h 0 0 0\n")
        fp.write(f"h 0 0 {z2}\n")
        fp.write(f"h 0 {y3} {z3}\n")
