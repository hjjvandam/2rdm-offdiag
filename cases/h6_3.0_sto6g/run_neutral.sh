. ../../../pypyscf/bin/activate
rm *.dat
for geom in ../h6_3.0/h6_0?????.xyz; do
    echo $geom
    python3 ../../src/2rdm-offdiag.py --charge 0 $geom "sto6g" h6-sto6g
done
