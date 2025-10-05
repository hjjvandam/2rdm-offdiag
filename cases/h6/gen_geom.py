#!/usr/bin/env python
"""
Script to generate random structures consisting of 4 Hydrogen atoms

The first atom is placed at the origin.
The second atom is placed along the z-axis up to +5 A
The thrid atom is placed within -5 to +5 A from the first along the z-axis
          and from 0 to 5 A along the y-axis
The fourth atom is placed within -5 to +5 A from the first along the z-axis
          and from -5 to +5 A along the y-axis
          and from 0 to +5 A along the x-axis
The fifth and sixth atom is placed within -5 to +5 A from the first along the z-axis
          and from -5 to +5 A along the y-axis
          and from -5 to +5 A along the x-axis
"""
import random

for ii in range(1000):
    z2 = random.uniform(0.0,5.0)
    z3 = random.uniform(-5.0,5.0)
    y3 = random.uniform(0.0,5.0)
    z4 = random.uniform(-5.0,5.0)
    y4 = random.uniform(-5.0,5.0)
    x4 = random.uniform(0.0,5.0)
    z5 = random.uniform(-5.0,5.0)
    y5 = random.uniform(-5.0,5.0)
    x5 = random.uniform(-5.0,5.0)
    z6 = random.uniform(-5.0,5.0)
    y6 = random.uniform(-5.0,5.0)
    x6 = random.uniform(-5.0,5.0)
    with open(f"h6-{ii:04d}.xyz","w") as fp:
        fp.write("6\n\n")
        fp.write("h 0 0 0\n")
        fp.write(f"h 0 0 {z2}\n")
        fp.write(f"h 0 {y3} {z3}\n")
        fp.write(f"h {x4} {y4} {z4}\n")
        fp.write(f"h {x5} {y5} {z5}\n")
        fp.write(f"h {x6} {y6} {z6}\n")
