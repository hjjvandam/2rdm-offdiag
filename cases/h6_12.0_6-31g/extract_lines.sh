#!/bin/bash
. ../../../pypyscf/bin/activate
#
# Closed shell a-a
#
../halfstraight_line.py r_h6_12.0-6-31g_aa_d_2200.dat
../straighthalf_line.py r_h6_12.0-6-31g_aa_d_2200.dat
../halfhalf_line.py     r_h6_12.0-6-31g_aa_d_2200.dat
#
# Closed shell a-b
#
../lowdin_shull_line.py r_h6_12.0-6-31g_ab_d_3025.dat
../halfstraight_line.py r_h6_12.0-6-31g_ab_d_3025.dat
../straighthalf_line.py r_h6_12.0-6-31g_ab_d_3025.dat
../halfhalf_line.py     r_h6_12.0-6-31g_ab_d_3025.dat
../eye_line.py          r_h6_12.0-6-31g_ab_o_3025.dat
#
# Open shell a-a
#
../halfstraight_line.py u_h6_12.0-6-31g_aa_d_2200.dat
../straighthalf_line.py u_h6_12.0-6-31g_aa_d_2200.dat
../onestraight_line.py  u_h6_12.0-6-31g_aa_d_2200.dat
../straightone_line.py  u_h6_12.0-6-31g_aa_d_2200.dat
#
# Open shell a-b
#
../lowdin_shull_line.py u_h6_12.0-6-31g_ab_d_3025.dat
../halfstraight_line.py u_h6_12.0-6-31g_ab_d_3025.dat
../straighthalf_line.py u_h6_12.0-6-31g_ab_d_3025.dat
../onestraight_line.py  u_h6_12.0-6-31g_ab_d_3025.dat
../straightone_line.py  u_h6_12.0-6-31g_ab_d_3025.dat
../eye_line.py          u_h6_12.0-6-31g_ab_o_3025.dat
