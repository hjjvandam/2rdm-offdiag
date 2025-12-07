#!/bin/bash
. ../../../pypyscf/bin/activate
#
# Closed shell a-b
#
../summarize_by_case.py --ls r_h4_12.0-6-31g_ab_d_1_ls_bc.dat \
                        --hh r_h4_12.0-6-31g_ab_d_1_hh_bc.dat \
                        | tee r_h4_12.0-6-31g_ab_d_1_summary.dat
#
# Open shell a-b
#
../summarize_by_case.py --ls u_h4_12.0-6-31g_ab_d_1_ls_bc.dat \
                        --hh u_h4_12.0-6-31g_ab_d_1_hh_bc.dat \
                        | tee u_h4_12.0-6-31g_ab_d_1_summary.dat
