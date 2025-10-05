../../src/2rdm-offdiag.py --overwrite True --charge 2 h4-00.44.xyz "cc-pvdz" h4-cc-pvdz
for geom in h4-0???.xyz; do
    echo $geom
    ../../src/2rdm-offdiag.py --charge 2 $geom "cc-pvdz" h4-cc-pvdz
done
