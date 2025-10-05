#!/bin/bash
for struct in h?_*.0; do
    mkdir ${struct}_6-31g
    cat > ${struct}_6-31g/run_neutral.sh << _EOF
. ../../../pypyscf/bin/activate
rm *.dat
for geom in ../${struct}/h?_0?????.xyz; do
    echo \$geom
    python3 ../../src/2rdm-offdiag.py --charge 0 \$geom "6-31g" ${struct}-6-31g
done
_EOF
    chmod +x ${struct}_6-31g/run_neutral.sh
done
