../../src/2rdm-offdiag.py --overwrite True --charge 0 ../h8/h8-00.44.xyz "cc-pvdz" h8-sto6g
for geom in ../h8/h8-0???.xyz; do
    echo $geom
    ../../src/2rdm-offdiag.py --charge 0 $geom "sto6g" h8-sto6g
done
