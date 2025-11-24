#!/bin/bash
. ../../../pypyscf/bin/activate
#
# Closed shell
#
../lowdin_shull_line.py r_h2_12.0-6-31g_ab_d_1.dat
../halfhalf_line.py     r_h2_12.0-6-31g_ab_d_1.dat
../eye_line.py          r_h2_12.0-6-31g_ab_o_1.dat
#
# Open shell
#
../lowdin_shull_line.py u_h2_12.0-6-31g_ab_d_1.dat
../halfhalf_line.py     u_h2_12.0-6-31g_ab_d_1.dat
../eye_line.py          u_h2_12.0-6-31g_ab_o_1.dat
