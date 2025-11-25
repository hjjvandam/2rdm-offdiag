#!/bin/bash
. ../../../pypyscf/bin/activate
for geoms in ../h4_12.0/h?_0?????.xyz; do
    geom=`basename $geoms`
    echo
    grep $geom u_h4_12.0-6-31g_aa_d_28_hs_bc.txt
    grep $geom u_h4_12.0-6-31g_aa_d_28_sh_bc.txt
    grep $geom u_h4_12.0-6-31g_aa_d_28_os_bc.txt
    grep $geom u_h4_12.0-6-31g_aa_d_28_so_bc.txt
    echo
    grep $geom u_h4_12.0-6-31g_ab_d_49_ls_bc.txt
    grep $geom u_h4_12.0-6-31g_ab_d_49_hs_bc.txt
    grep $geom u_h4_12.0-6-31g_ab_d_49_sh_bc.txt
    grep $geom u_h4_12.0-6-31g_ab_d_49_os_bc.txt
    grep $geom u_h4_12.0-6-31g_ab_d_49_so_bc.txt
    echo
done
