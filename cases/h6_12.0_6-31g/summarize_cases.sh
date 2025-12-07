#!/bin/bash
. ../../../pypyscf/bin/activate
#
# Closed shell a-a
#
../summarize_by_case.py --sh r_h6_12.0-6-31g_aa_d_2200_sh_bc.dat \
                        --hs r_h6_12.0-6-31g_aa_d_2200_hs_bc.dat \
                        --hh r_h6_12.0-6-31g_aa_d_2200_hh_bc.dat \
                        | tee r_h6_12.0-6-31g_aa_d_2200_summary.dat
#
# Closed shell a-b
#
../summarize_by_case.py --ls r_h6_12.0-6-31g_ab_d_3025_ls_bc.dat \
                        --sh r_h6_12.0-6-31g_ab_d_3025_sh_bc.dat \
                        --hs r_h6_12.0-6-31g_ab_d_3025_hs_bc.dat \
                        --hh r_h6_12.0-6-31g_ab_d_3025_hh_bc.dat \
                        | tee r_h6_12.0-6-31g_ab_d_3025_summary.dat
#
# Open shell a-a
#
../summarize_by_case.py --sh u_h6_12.0-6-31g_aa_d_2200_sh_bc.dat \
                        --hs u_h6_12.0-6-31g_aa_d_2200_hs_bc.dat \
                        --so u_h6_12.0-6-31g_aa_d_2200_so_bc.dat \
                        --os u_h6_12.0-6-31g_aa_d_2200_os_bc.dat \
                        | tee u_h6_12.0-6-31g_aa_d_2200_summary.dat
#
# Open shell a-b
#
../summarize_by_case.py --ls u_h6_12.0-6-31g_ab_d_3025_ls_bc.dat \
                        --sh u_h6_12.0-6-31g_ab_d_3025_sh_bc.dat \
                        --hs u_h6_12.0-6-31g_ab_d_3025_hs_bc.dat \
                        --so u_h6_12.0-6-31g_ab_d_3025_so_bc.dat \
                        --os u_h6_12.0-6-31g_ab_d_3025_os_bc.dat \
                        | tee u_h6_12.0-6-31g_ab_d_3025_summary.dat
