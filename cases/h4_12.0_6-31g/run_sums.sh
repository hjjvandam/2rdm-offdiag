#!/bin/bash
echo
echo "closed shell a-a hs, sh, hh"
echo
../sum_rdm.py r_h4_12.0-6-31g_aa_d_28.dat
../sum_rdm.py r_h4_12.0-6-31g_aa_d_28_hs.dat
../sum_rdm.py r_h4_12.0-6-31g_aa_d_28_sh.dat
../sum_rdm.py r_h4_12.0-6-31g_aa_d_28_hh.dat
echo
echo "closed shell a-b ls, hs, sh, hh"
echo
../sum_rdm.py r_h4_12.0-6-31g_ab_d_49.dat
../sum_rdm.py r_h4_12.0-6-31g_ab_d_49_ls.dat
../sum_rdm.py r_h4_12.0-6-31g_ab_d_49_hs.dat
../sum_rdm.py r_h4_12.0-6-31g_ab_d_49_sh.dat
../sum_rdm.py r_h4_12.0-6-31g_ab_d_49_hh.dat
echo
echo
echo "open shell a-a hs, sh, os, so"
echo
../sum_rdm.py u_h4_12.0-6-31g_aa_d_28.dat
../sum_rdm.py u_h4_12.0-6-31g_aa_d_28_hs.dat
../sum_rdm.py u_h4_12.0-6-31g_aa_d_28_sh.dat
../sum_rdm.py u_h4_12.0-6-31g_aa_d_28_os.dat
../sum_rdm.py u_h4_12.0-6-31g_aa_d_28_so.dat
echo
echo "open shell a-b ls, hs, sh, os, so"
echo
../sum_rdm.py u_h4_12.0-6-31g_ab_d_49.dat
../sum_rdm.py u_h4_12.0-6-31g_ab_d_49_ls.dat
../sum_rdm.py u_h4_12.0-6-31g_ab_d_49_hs.dat
../sum_rdm.py u_h4_12.0-6-31g_ab_d_49_sh.dat
../sum_rdm.py u_h4_12.0-6-31g_ab_d_49_os.dat
../sum_rdm.py u_h4_12.0-6-31g_ab_d_49_so.dat
