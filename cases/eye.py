import math
"""
Due to the shape of the correlation effects we refer to this as the Eye.

This little program generates the points of the two lines that enclose
the correlation contributions of the 2-electron density matrices.
The function lies along the line y==1-x. Somehow GNUplot cannot draw
functions that are lines in a 3D plot. So I am forced to write the
positions of the line out explicitly such that GNUplot can plot this
data set.
"""

def corr(x,y):
    """
    The correlation function.
    """
    res = math.sqrt(math.sqrt(x*(1.0-x)*y*(1.0-y)))
    return res

def generator(fp,sign):
    """
    Generate and write the data
    """
    #
    # range() works with integers and doesn't work with
    # floats. So we use integers in the range and convert
    # them to floats.
    #
    for q in range(0,101):
        x=(1.0*q)/100.0
        y=(1.0-x)
        z=sign*corr(x,y)
        fp.write(f"{x} {y} {z}\n")

with open("corr_pos.dat","w") as fp:
    generator(fp,1.0)

with open("corr_neg.dat","w") as fp:
    generator(fp,-1.0)
