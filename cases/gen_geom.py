#!/usr/bin/env python
"""
Generate structure with a number of H atoms

The aim is to generate structures such that the average density is
constant independent of the number of atoms included.

This way we can generate structures with fewer atoms by just keeping
the first N many atoms.

The process for generating a single structure is to start at
the origin. Then we add atoms by randomly choosing polar
coordinates for each. We sort the list of atoms according to
distance from the origin.

We check the density for a given number of atoms by finding the
distance to the origin for the corresponding atom. Then we
divide the number of atoms within the sphere by the volume of the
sphere. We average the density for a given number of atoms
across all structures. We do this calculation for increasing
numbers of atoms and check the results.
"""
import json
import math
import numpy as np
import os
import pathlib
import random
import sys

def generate_structure(natoms,rmax):
    """
    Generate a structure with natoms atoms by random selection of polar coordinates
    """
    positions = []
    rr = []
    for iatom in range(natoms):
        r = math.cbrt(random.random())*rmax
        t = random.uniform(0.0,math.pi)
        a = random.uniform(0.0,math.pi*2.0)
        x = r*math.sin(t)*math.cos(a)
        y = r*math.sin(t)*math.sin(a)
        z = r*math.cos(t)
        if len(rr) == 0:
            rr.append(r)
            positions.append((x,y,z))
        elif r > rr[-1]:
            rr.append(r)
            positions.append((x,y,z))
        else:
            for ii in range(len(rr)):
                if r < rr[ii]:
                    rr.insert(ii,r)
                    positions.insert(ii,(x,y,z))
                    break
    return (positions,rr)

def density(tab_in,inc):
    """
    Compute the density
    """
    tab_out = []
    num = 1
    for rr in tab_in[1:]:
        num += 1
        dens = (1.0*num)/(math.pi*4.0/3.0*(rr**3))
        if num%inc == 0:
            tab_out.append(dens)
    return tab_out

def avg_density(tab_in):
    """
    Compute a table of average densities

    Tab_in is table where every row corresponds to
    the density of a number of atoms. Here we average
    the densities over all rows.
    """
    num_rows = len(tab_in)
    size_table = len(tab_in[0])
    avg_dens = np.zeros(size_table)
    for row in tab_in:
        for ii in range(size_table):
            avg_dens[ii] += row[ii]
    for ii in range(size_table):
        avg_dens[ii] *= 1.0/num_rows
    return avg_dens

def write_geometries(name,rmax,number,positions,inc):
    """
    Write geometries given a list of positions

    The positions are stored in files in directories.
    The directory name consists of `name`, and the
    number of atoms. Within that directory the
    filename consists of the `name`, the number of
    atoms, and the geometry number.
    """
    num_structs = len(positions)
    natoms = len(positions[0])
    dir_names = []
    ii = inc
    while ii <= natoms:
        dir_name = f"{name}{ii}_{str(rmax)}"
        dir_names.append(dir_name)
        if not os.path.exists(dir_name):
            pathlib.Path(dir_name).mkdir(exist_ok=True)
        ii += inc
    jj = -1
    for pos in positions:
        jj += 1
        ii = inc
        kk = -1
        while ii <= natoms:
            kk += 1
            dir_name = dir_names[kk]
            file_name = f"{dir_name}/h{ii}_{jj:06d}.xyz"
            with open(file_name,"w") as fp:
                fp.write(f"{ii}\n\n")
                for iat in range(ii):
                    (xx,yy,zz) = pos[iat]
                    fp.write(f"H {rmax*xx:14.6f} {rmax*yy:14.6f} {rmax*zz:14.6f}\n")
            ii += inc

def generate_structures_with_rmax(rmax,number,natoms):
    """
    For a given maximum radius generate `number` of structures

    The results are returned in two lists:
    - a list of structures, where each structure is a list of points
    - a list of rows, where each row is a list of structure radii
    """
    inc = 2
    structs = []
    rows = []
    for ii in range(number):
        (positions,rr) = generate_structure(natoms,rmax)
        structs.append(positions)
        rows.append(rr)
    dens = []
    for rr in rows:
        res = density(rr,inc)
        dens.append(res)
    avg_dens = avg_density(dens)
    return (structs,rows,avg_dens)

number = 1000 # molecular structures
natoms = 8
if pathlib.Path("./points_inside_unit_sphere.json").is_file():
    with open("./points_inside_unit_sphere.json","r") as fp:
        structs = json.load(fp)
else:
    (structs,rows,avg_dens) = generate_structures_with_rmax(1.0,number,natoms)
    print(avg_dens)
    structs = json.loads(json.dumps(structs))
    with open("./points_inside_unit_sphere.json","w") as fp:
        json.dump(structs,fp)
#sys.exit(10)
inc = 2
rmax = 1.5
write_geometries("H",rmax,number,structs,inc)
#
rmax = 3.0
write_geometries("H",rmax,number,structs,inc)
#
#rmax = 4.0
#write_geometries("H",rmax,number,structs,inc)
#
#rmax = 5.0
#write_geometries("H",rmax,number,structs,inc)
#
rmax = 6.0
write_geometries("H",rmax,number,structs,inc)
#
rmax = 9.0
write_geometries("H",rmax,number,structs,inc)
#
rmax = 12.0
write_geometries("H",rmax,number,structs,inc)
