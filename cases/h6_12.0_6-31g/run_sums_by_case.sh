#!/bin/bash
. ../../../pypyscf/bin/activate
#
# Closed shell a-a
#
../sum_rdm_by_case.py r_h6_12.0-6-31g_aa_d_2200.dat    | tee r_h6_12.0-6-31g_aa_d_2200_bc.dat
../sum_rdm_by_case.py r_h6_12.0-6-31g_aa_d_2200_hs.dat | tee r_h6_12.0-6-31g_aa_d_2200_hs_bc.dat
../sum_rdm_by_case.py r_h6_12.0-6-31g_aa_d_2200_sh.dat | tee r_h6_12.0-6-31g_aa_d_2200_sh_bc.dat
../sum_rdm_by_case.py r_h6_12.0-6-31g_aa_d_2200_hh.dat | tee r_h6_12.0-6-31g_aa_d_2200_hh_bc.dat
#
# Closed shell a-b
#
../sum_rdm_by_case.py r_h6_12.0-6-31g_ab_d_3025.dat    | tee r_h6_12.0-6-31g_ab_d_3025_bc.dat
../sum_rdm_by_case.py r_h6_12.0-6-31g_ab_d_3025_ls.dat | tee r_h6_12.0-6-31g_ab_d_3025_ls_bc.dat
../sum_rdm_by_case.py r_h6_12.0-6-31g_ab_d_3025_hs.dat | tee r_h6_12.0-6-31g_ab_d_3025_hs_bc.dat
../sum_rdm_by_case.py r_h6_12.0-6-31g_ab_d_3025_sh.dat | tee r_h6_12.0-6-31g_ab_d_3025_sh_bc.dat
../sum_rdm_by_case.py r_h6_12.0-6-31g_ab_d_3025_hh.dat | tee r_h6_12.0-6-31g_ab_d_3025_hh_bc.dat
../sum_rdm_by_case.py r_h6_12.0-6-31g_ab_o_3025_en.dat | tee r_h6_12.0-6-31g_ab_o_3025_en_bc.dat
#
# Open shell a-a
#
../sum_rdm_by_case.py u_h6_12.0-6-31g_aa_d_2200.dat    | tee u_h6_12.0-6-31g_aa_d_2200_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_aa_d_2200_hs.dat | tee u_h6_12.0-6-31g_aa_d_2200_hs_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_aa_d_2200_sh.dat | tee u_h6_12.0-6-31g_aa_d_2200_sh_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_aa_d_2200_os.dat | tee u_h6_12.0-6-31g_aa_d_2200_os_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_aa_d_2200_so.dat | tee u_h6_12.0-6-31g_aa_d_2200_so_bc.dat
#
# Open shell a-b
#
../sum_rdm_by_case.py u_h6_12.0-6-31g_ab_d_3025.dat    | tee u_h6_12.0-6-31g_ab_d_3025_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_ab_d_3025_ls.dat | tee u_h6_12.0-6-31g_ab_d_3025_ls_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_ab_d_3025_hs.dat | tee u_h6_12.0-6-31g_ab_d_3025_hs_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_ab_d_3025_sh.dat | tee u_h6_12.0-6-31g_ab_d_3025_sh_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_ab_d_3025_os.dat | tee u_h6_12.0-6-31g_ab_d_3025_os_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_ab_d_3025_so.dat | tee u_h6_12.0-6-31g_ab_d_3025_so_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_ab_o_3025_en.dat | tee u_h6_12.0-6-31g_ab_o_3025_en_bc.dat
../sum_rdm_by_case.py u_h6_12.0-6-31g_ab_o_3025_ep.dat | tee u_h6_12.0-6-31g_ab_o_3025_ep_bc.dat
