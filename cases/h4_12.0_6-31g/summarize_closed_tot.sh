#!/bin/bash
. ../../../pypyscf/bin/activate
for geoms in ../h4_12.0/h?_0?????.xyz; do
    geom=`basename $geoms`
    grep $geom r_h4_12.0-6-31g_aa_d_28_bc.txt
    grep $geom r_h4_12.0-6-31g_ab_d_49_bc.txt
    echo
done
