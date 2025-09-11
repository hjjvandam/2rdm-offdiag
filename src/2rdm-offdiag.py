#!python3
"""
Script to extract 2RDM elements as a function of 1RDM occupation numbers.

Command line arguments:

- XYZ-file name
- basis set
- molecular charge (default 0)
- spin multiplicity (default 1)
"""
import argparse
import math
import numpy as np
from pyscf import gto, scf, fci, ao2mo

def get_molecule(xyz_file,basis_set,nopen,charge):
    """
    Construct the molecule to do the calculation on

    This function reads the molecular structure and the basis set.
    Then it takes the number of open shell orbitals and the
    molecular charge. With all the combined it constructs and
    returns the molecule object.
    """
    mol = gto.Mole(atom=xyz_file,basis=basis_set)
    mol.charge = charge
    mol.spin = nopen
    mol.build()
    return mol

def calc_wfn(mol):
    """
    Calculate the Full-CI wavefunction in natural orbital basis
    """
    uhf_wf = scf.UHF(mol).run()
    fci_wf = fci.FCI(uhf_wf)
    norb = mol.nao
    nelec = mol.nelec
    (E_fci,C_fci) = fci_wf.kernel()
    print(f"converged FCI energy in SCF orbital basis = {E_fci}")
    (rdm1_a,rdm1_b) = fci_wf.make_rdm1s(C_fci,norb,nelec)
    #
    (occ,orbs) = np.linalg.eigh(rdm1_a)
    uhf_wf.mo_coeff[0] = np.matmul(uhf_wf.mo_coeff[0],orbs)
    #
    (occ,orbs) = np.linalg.eigh(rdm1_b)
    uhf_wf.mo_coeff[1] = np.matmul(uhf_wf.mo_coeff[1],orbs)
    #
    fci_wf = fci.FCI(uhf_wf)
    (E_fci,C_fci) = fci_wf.kernel()
    print(f"converged FCI energy in nat orbital basis = {E_fci}")
    return (fci_wf,C_fci)

def calc_rdms(fci_wf,C_fci,mol):
    """
    Calculate and return the 1- and 2-electron density matrices

    We do transpose the matrices so that the occupations are on the
    diagonal.
    """
    norb = mol.nao
    nelec = mol.nelec
    ((rdm1_a,rdm1_b),(rdm2_aa,rdm2_ab,rdm2_bb)) = fci_wf.make_rdm12s(C_fci,norb,nelec)
    # electron ordering is (1,1) (2,2)
    rdm2_aa = rdm2_aa.transpose(0,2,1,3) # electron ordering now is (1,2) (1,2)
    rdm2_ab = rdm2_ab.transpose(0,2,1,3)
    rdm2_bb = rdm2_bb.transpose(0,2,1,3)
    return (rdm1_a,rdm1_b,rdm2_aa,rdm2_ab,rdm2_bb)

def extract_elements(name,mode,rdm1_a,rdm1_b,rdm2_aa,rdm2_ab,rdm2_bb,mol):
    """
    Extract density matrix elements

    Write out diagonal and off-diagonal elements as function of the occupation
    numbers.
    """
    norb = mol.nao
    nelec = mol.nelec
    (nel_a, nel_b) = nelec
    if nel_a < 2:
        nterms_aa = 0
    else:
        nterms_aa = math.comb(norb-2,nel_a-2)*math.comb(norb,nel_b)
    if nel_a < 1 or nel_b < 1:
        nterms_ab = 0
    else:
        nterms_ab = math.comb(norb-1,nel_a-1)*math.comb(norb-1,nel_b-1)
    if nel_b < 2:
        nterms_bb = 0
    else:
        nterms_bb = math.comb(norb,nel_a)*math.comb(norb-2,nel_b-2)
    filename = f"{name}_aa_d_{nterms_aa}.dat"
    with open(filename,mode) as fp:
        for ii in range(norb):
            for jj in range(norb):
                occ_a1 = rdm1_a[ii,ii]
                occ_a2 = rdm1_a[jj,jj]
                diag   = rdm2_aa[ii,jj,ii,jj]
                if ii < norb - nel_a:
                    typi = "virt"
                else:
                    typi = "occ."
                if jj < norb - nel_a:
                    typj = "virt"
                else:
                    typj = "occ."
                fp.write(f"{occ_a1:.16f} {occ_a2:.16f} {diag:20.16f} # {ii:4d} {jj:4d} {typi} {typj}\n")
    filename = f"{name}_aa_o_{nterms_aa}.dat"
    with open(filename,mode) as fp:
        for ii in range(norb):
            for jj in range(norb):
                if not (ii == jj):
                    occ_a1 = rdm1_a[ii,ii]
                    occ_a2 = rdm1_a[jj,jj]
                    odiag  = rdm2_aa[ii,ii,jj,jj]
                    if ii < norb - nel_a:
                        typi = "virt"
                    else:
                        typi = "occ."
                    if jj < norb - nel_a:
                        typj = "virt"
                    else:
                        typj = "occ."
                    fp.write(f"{occ_a1:.16f} {occ_a2:.16f} {odiag:20.16f} # {ii:4d} {jj:4d} {typi} {typj}\n")
    filename = f"{name}_ab_d_{nterms_ab}.dat"
    with open(filename,mode) as fp:
        for ii in range(norb):
            for jj in range(norb):
                occ_a = rdm1_a[ii,ii]
                occ_b = rdm1_b[jj,jj]
                diag  = rdm2_ab[ii,jj,ii,jj]
                if ii < norb - nel_a:
                    typi = "virt"
                else:
                    typi = "occ."
                if jj < norb - nel_b:
                    typj = "virt"
                else:
                    typj = "occ."
                fp.write(f"{occ_a:.16f} {occ_b:.16f} {diag:20.16f} # {ii:4d} {jj:4d} {typi} {typj}\n")
    filename = f"{name}_ab_o_{nterms_ab}.dat"
    with open(filename,mode) as fp:
        for ii in range(norb):
            for jj in range(norb):
                if not (ii == jj):
                    occ_a = rdm1_a[ii,ii]
                    occ_b = rdm1_b[jj,jj]
                    odiag = rdm2_ab[ii,ii,jj,jj]
                    if ii < norb - nel_a:
                        typi = "virt"
                    else:
                        typi = "occ."
                    if jj < norb - nel_b:
                        typj = "virt"
                    else:
                        typj = "occ."
                    fp.write(f"{occ_a:.16f} {occ_b:.16f} {odiag:20.16f} # {ii:4d} {jj:4d} {typi} {typj}\n")
    filename = f"{name}_bb_d_{nterms_bb}.dat"
    with open(filename,mode) as fp:
        for ii in range(norb):
            for jj in range(norb):
                occ_b1 = rdm1_b[ii,ii]
                occ_b2 = rdm1_b[jj,jj]
                diag   = rdm2_bb[ii,jj,ii,jj]
                if ii < norb - nel_b:
                    typi = "virt"
                else:
                    typi = "occ."
                if jj < norb - nel_b:
                    typj = "virt"
                else:
                    typj = "occ."
                fp.write(f"{occ_b1:.16f} {occ_b2:.16f} {diag:20.16f} # {ii:4d} {jj:4d} {typi} {typj}\n")
    filename = f"{name}_bb_o_{nterms_bb}.dat"
    with open(filename,mode) as fp:
        for ii in range(norb):
            for jj in range(norb):
                if not (ii == jj):
                    occ_b1 = rdm1_b[ii,ii]
                    occ_b2 = rdm1_b[jj,jj]
                    odiag  = rdm2_bb[ii,ii,jj,jj]
                    if ii < norb - nel_b:
                        typi = "virt"
                    else:
                        typi = "occ."
                    if jj < norb - nel_b:
                        typj = "virt"
                    else:
                        typj = "occ."
                    fp.write(f"{occ_b1:.16f} {occ_b2:.16f} {odiag:20.16f} # {ii:4d} {jj:4d} {typi} {typj}\n")

def do_all(xyz_file,prefix_out,basis_set,nopen,charge,mode):
    """
    Do the whole thing
    """
    mol = get_molecule(xyz_file,basis_set,nopen,charge)
    (fci_wf,C_fci) = calc_wfn(mol)
    (rdm1_a,rdm1_b,rdm2_aa,rdm2_ab,rdm2_bb) = calc_rdms(fci_wf,C_fci,mol)
    extract_elements(prefix_out,mode,rdm1_a,rdm1_b,rdm2_aa,rdm2_ab,rdm2_bb,mol)

def commandline_args():
    parser = argparse.ArgumentParser(
             prog="2RDM-offdiag",
             description="Calculate 2RDM elements and list them as functions of occupation numbers",
             epilog="DON'T PANIC")
    parser.add_argument("XYZ_file",help="the XYZ file with the molecular structure")
    parser.add_argument("basis_set",help="the Gaussian basis set name")
    parser.add_argument("output_prefix",help="the prefix for the output files")
    parser.add_argument("-m","--mult",help="spin multiplicity",type=int,default=1)
    parser.add_argument("-c","--charge",help="molecular charge",type=int,default=0)
    parser.add_argument("--overwrite",help="overwrite the data files",type=bool,default=False)
    return parser.parse_args()

if __name__ == "__main__":
    args = commandline_args()
    xyz_file = args.XYZ_file
    basis_set = args.basis_set
    prefix_out = args.output_prefix
    mult = args.mult
    nopen = mult-1
    charge = args.charge
    mode = "a"
    if args.overwrite:
        mode = "w"
    if nopen < 0:
        print(f"Number of unpaired electron is: {nopen}?")
        exit()
    do_all(xyz_file,prefix_out,basis_set,nopen,charge,mode)
