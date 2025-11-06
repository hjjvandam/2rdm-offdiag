. ../../../pypyscf/bin/activate
rm *.dat
for geom in ../h8_3.0/h8_0?????.xyz; do
    echo $geom
    python3 ../../src/2rdm-offdiag.py --charge 0 $geom "sto6g" h8-sto6g
done
