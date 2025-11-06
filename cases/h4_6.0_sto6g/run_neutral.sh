. ../../../pypyscf/bin/activate
rm *.dat
for geom in ../h4_6.0/h4_0?????.xyz; do
    echo $geom
    python3 ../../src/2rdm-offdiag.py --charge 0 $geom "sto6g" h4-sto6g
done
