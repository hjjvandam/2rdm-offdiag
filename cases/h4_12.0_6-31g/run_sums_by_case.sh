#!/bin/bash
echo
echo "closed shell a-a hs, sh, hh"
echo
../sum_rdm_by_case.py r_h4_12.0-6-31g_aa_d_28.dat    | tee r_h4_12.0-6-31g_aa_d_28_bc.dat
../sum_rdm_by_case.py r_h4_12.0-6-31g_aa_d_28_hs.dat | tee r_h4_12.0-6-31g_aa_d_28_hs_bc.dat
../sum_rdm_by_case.py r_h4_12.0-6-31g_aa_d_28_sh.dat | tee r_h4_12.0-6-31g_aa_d_28_sh_bc.dat
../sum_rdm_by_case.py r_h4_12.0-6-31g_aa_d_28_hh.dat | tee r_h4_12.0-6-31g_aa_d_28_hh_bc.dat
echo
echo "closed shell a-b ls, hs, sh, hh, en"
echo
../sum_rdm_by_case.py r_h4_12.0-6-31g_ab_d_49.dat    | tee r_h4_12.0-6-31g_ab_d_49_bc.dat
../sum_rdm_by_case.py r_h4_12.0-6-31g_ab_d_49_ls.dat | tee r_h4_12.0-6-31g_ab_d_49_ls_bc.dat
../sum_rdm_by_case.py r_h4_12.0-6-31g_ab_d_49_hs.dat | tee r_h4_12.0-6-31g_ab_d_49_hs_bc.dat
../sum_rdm_by_case.py r_h4_12.0-6-31g_ab_d_49_sh.dat | tee r_h4_12.0-6-31g_ab_d_49_sh_bc.dat
../sum_rdm_by_case.py r_h4_12.0-6-31g_ab_d_49_hh.dat | tee r_h4_12.0-6-31g_ab_d_49_hh_bc.dat
../sum_rdm_by_case.py r_h4_12.0-6-31g_ab_o_49_en.dat | tee r_h4_12.0-6-31g_ab_o_49_en_bc.dat
echo
echo
echo "open shell a-a hs, sh, os, so"
echo
../sum_rdm_by_case.py u_h4_12.0-6-31g_aa_d_28.dat    | tee u_h4_12.0-6-31g_aa_d_28_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_aa_d_28_hs.dat | tee u_h4_12.0-6-31g_aa_d_28_hs_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_aa_d_28_sh.dat | tee u_h4_12.0-6-31g_aa_d_28_sh_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_aa_d_28_os.dat | tee u_h4_12.0-6-31g_aa_d_28_os_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_aa_d_28_so.dat | tee u_h4_12.0-6-31g_aa_d_28_so_bc.dat
echo
echo "open shell a-b ls, hs, sh, os, so, en, ep"
echo
../sum_rdm_by_case.py u_h4_12.0-6-31g_ab_d_49.dat    | tee u_h4_12.0-6-31g_ab_d_49_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_ab_d_49_ls.dat | tee u_h4_12.0-6-31g_ab_d_49_ls_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_ab_d_49_hs.dat | tee u_h4_12.0-6-31g_ab_d_49_hs_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_ab_d_49_sh.dat | tee u_h4_12.0-6-31g_ab_d_49_sh_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_ab_d_49_os.dat | tee u_h4_12.0-6-31g_ab_d_49_os_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_ab_d_49_so.dat | tee u_h4_12.0-6-31g_ab_d_49_so_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_ab_o_49_en.dat | tee u_h4_12.0-6-31g_ab_o_49_en_bc.dat
../sum_rdm_by_case.py u_h4_12.0-6-31g_ab_o_49_ep.dat | tee u_h4_12.0-6-31g_ab_o_49_ep_bc.dat
