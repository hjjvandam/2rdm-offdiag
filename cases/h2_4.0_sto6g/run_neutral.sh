. ../../../pypyscf/bin/activate
rm *.dat
for geom in ../h2_4.0/h2_0?????.xyz; do
    echo $geom
    python3 ../../src/2rdm-offdiag.py --charge 0 $geom "sto6g" h2-sto6g
done
