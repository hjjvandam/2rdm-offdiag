#!/bin/bash
. ~/Documents/pypyscf/bin/activate
../eye_line.py r_h6_3.0-6-31g_ab_o_3025.dat
cat r_h6_3.0-6-31g_ab_o_3025_en.dat r_h6_3.0-6-31g_ab_o_3025_nen.dat > r_h6_3.0-6-31g_ab_o_3025_eye.dat
sort -k1,2 -n r_h6_3.0-6-31g_ab_o_3025_eye.dat > r_h6_3.0-6-31g_ab_o_3025_eye_sorted.dat
