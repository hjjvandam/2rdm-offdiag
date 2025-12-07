#!/bin/bash
echo
echo "closed shell a-b ls, hs, sh, hh, en"
echo
../sum_rdm_by_case.py r_h2_12.0-6-31g_ab_d_1.dat    | tee r_h2_12.0-6-31g_ab_d_1_bc.dat
../sum_rdm_by_case.py r_h2_12.0-6-31g_ab_d_1_ls.dat | tee r_h2_12.0-6-31g_ab_d_1_ls_bc.dat
../sum_rdm_by_case.py r_h2_12.0-6-31g_ab_d_1_hh.dat | tee r_h2_12.0-6-31g_ab_d_1_hh_bc.dat
../sum_rdm_by_case.py r_h2_12.0-6-31g_ab_o_1_en.dat | tee r_h2_12.0-6-31g_ab_o_1_en_bc.dat
echo
echo
echo "open shell a-b ls, hs, sh, os, so, en, ep"
echo
../sum_rdm_by_case.py u_h2_12.0-6-31g_ab_d_1.dat    | tee u_h2_12.0-6-31g_ab_d_1_bc.dat
../sum_rdm_by_case.py u_h2_12.0-6-31g_ab_d_1_ls.dat | tee u_h2_12.0-6-31g_ab_d_1_ls_bc.dat
../sum_rdm_by_case.py u_h2_12.0-6-31g_ab_d_1_hh.dat | tee u_h2_12.0-6-31g_ab_d_1_hh_bc.dat
../sum_rdm_by_case.py u_h2_12.0-6-31g_ab_o_1_en.dat | tee u_h2_12.0-6-31g_ab_o_1_en_bc.dat
../sum_rdm_by_case.py u_h2_12.0-6-31g_ab_o_1_ep.dat | tee u_h2_12.0-6-31g_ab_o_1_ep_bc.dat
