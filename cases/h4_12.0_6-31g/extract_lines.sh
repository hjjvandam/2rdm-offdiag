#!/bin/bash
. ../../../pypyscf/bin/activate
#
# Closed shell a-a
#
../halfstraight_line.py r_h4_12.0-6-31g_aa_d_28.dat
../straighthalf_line.py r_h4_12.0-6-31g_aa_d_28.dat
../halfhalf_line.py     r_h4_12.0-6-31g_aa_d_28.dat
#
# Closed shell a-b
#
../lowdin_shull_line.py r_h4_12.0-6-31g_ab_d_49.dat
../halfstraight_line.py r_h4_12.0-6-31g_ab_d_49.dat
../straighthalf_line.py r_h4_12.0-6-31g_ab_d_49.dat
../halfhalf_line.py     r_h4_12.0-6-31g_ab_d_49.dat
../eye_line.py          r_h4_12.0-6-31g_ab_o_49.dat
#
# Open shell a-a
#
../halfstraight_line.py u_h4_12.0-6-31g_aa_d_28.dat
../straighthalf_line.py u_h4_12.0-6-31g_aa_d_28.dat
../onestraight_line.py  u_h4_12.0-6-31g_aa_d_28.dat
../straightone_line.py  u_h4_12.0-6-31g_aa_d_28.dat
#
# Open shell a-b
#
../lowdin_shull_line.py u_h4_12.0-6-31g_ab_d_49.dat
../halfstraight_line.py u_h4_12.0-6-31g_ab_d_49.dat
../straighthalf_line.py u_h4_12.0-6-31g_ab_d_49.dat
../onestraight_line.py  u_h4_12.0-6-31g_ab_d_49.dat
../straightone_line.py  u_h4_12.0-6-31g_ab_d_49.dat
../eye_line.py          u_h4_12.0-6-31g_ab_o_49.dat
