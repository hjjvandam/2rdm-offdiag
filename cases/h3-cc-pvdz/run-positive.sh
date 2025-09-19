../../src/2rdm-offdiag.py --overwrite True --charge 1 h3-00.82.xyz "cc-pvdz" h3-cc-pvdz
for geom in h3-0???.xyz; do
    ../../src/2rdm-offdiag.py --charge 1 $geom "cc-pvdz" h3-cc-pvdz
done
