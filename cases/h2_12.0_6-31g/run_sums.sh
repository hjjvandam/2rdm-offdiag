#!/bin/bash
echo
echo "closed shell"
echo
../sum_rdm.py r_h2_12.0-6-31g_ab_d_1.dat
../sum_rdm.py r_h2_12.0-6-31g_ab_d_1_ls.dat
../sum_rdm.py r_h2_12.0-6-31g_ab_d_1_hh.dat
../sum_rdm.py r_h2_12.0-6-31g_ab_d_1_nls.dat
echo
echo
echo "open shell"
echo
../sum_rdm.py u_h2_12.0-6-31g_ab_d_1.dat
../sum_rdm.py u_h2_12.0-6-31g_ab_d_1_ls.dat
../sum_rdm.py u_h2_12.0-6-31g_ab_d_1_hh.dat
../sum_rdm.py u_h2_12.0-6-31g_ab_d_1_nls.dat
