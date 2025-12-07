#!/bin/bash
. ../../../pypyscf/bin/activate
#
# Closed shell a-a
#
../summarize_by_case.py --sh r_h4_12.0-6-31g_aa_d_28_sh_bc.dat \
                        --hs r_h4_12.0-6-31g_aa_d_28_hs_bc.dat \
                        --hh r_h4_12.0-6-31g_aa_d_28_hh_bc.dat \
                        | tee r_h4_12.0-6-31g_aa_d_28_summary.dat
#
# Closed shell a-b
#
../summarize_by_case.py --ls r_h4_12.0-6-31g_ab_d_49_ls_bc.dat \
                        --sh r_h4_12.0-6-31g_ab_d_49_sh_bc.dat \
                        --hs r_h4_12.0-6-31g_ab_d_49_hs_bc.dat \
                        --hh r_h4_12.0-6-31g_ab_d_49_hh_bc.dat \
                        | tee r_h4_12.0-6-31g_ab_d_49_summary.dat
#
# Open shell a-a
#
../summarize_by_case.py --sh u_h4_12.0-6-31g_aa_d_28_sh_bc.dat \
                        --hs u_h4_12.0-6-31g_aa_d_28_hs_bc.dat \
                        --so u_h4_12.0-6-31g_aa_d_28_so_bc.dat \
                        --os u_h4_12.0-6-31g_aa_d_28_os_bc.dat \
                        | tee u_h4_12.0-6-31g_aa_d_28_summary.dat
#
# Open shell a-b
#
../summarize_by_case.py --ls u_h4_12.0-6-31g_ab_d_49_ls_bc.dat \
                        --sh u_h4_12.0-6-31g_ab_d_49_sh_bc.dat \
                        --hs u_h4_12.0-6-31g_ab_d_49_hs_bc.dat \
                        --so u_h4_12.0-6-31g_ab_d_49_so_bc.dat \
                        --os u_h4_12.0-6-31g_ab_d_49_os_bc.dat \
                        | tee u_h4_12.0-6-31g_ab_d_49_summary.dat
