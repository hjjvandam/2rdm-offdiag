. ../../../pypyscf/bin/activate
rm *.dat
for geom in ../h4_4.0/h?_0?????.xyz; do
    echo $geom
    python3 ../../src/2rdm-offdiag.py --charge 0 $geom "6-31g" h4_4.0-6-31g
done
