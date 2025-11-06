#!/bin/bash
folders=(h2_3.0_sto6g h2_4.0_sto6g h2_5.0_sto6g h2_6.0_sto6g h2_12.0_sto6g
         h4_3.0_sto6g h4_4.0_sto6g h4_5.0_sto6g h4_6.0_sto6g h4_12.0_sto6g
         h6_3.0_sto6g h6_4.0_sto6g h6_5.0_sto6g h6_6.0_sto6g h6_12.0_sto6g
         h8_3.0_sto6g h8_4.0_sto6g h8_5.0_sto6g h8_6.0_sto6g h8_12.0_sto6g
         h2_3.0_6-31g h2_4.0_6-31g h2_5.0_6-31g h2_6.0_6-31g h2_12.0_6-31g
         h4_3.0_6-31g h4_4.0_6-31g h4_5.0_6-31g h4_6.0_6-31g h4_12.0_6-31g
         h6_3.0_6-31g h6_4.0_6-31g h6_5.0_6-31g h6_6.0_6-31g h6_12.0_6-31g
         h8_3.0_6-31g h8_4.0_6-31g h8_5.0_6-31g h8_6.0_6-31g h8_12.0_6-31g)
path=`pwd`
for folder in "${folders[@]}"; do
    echo $folder
    cd $path/$folder
    ./run_neutral.sh 2>&1 | /usr/bin/tee run_neutral.log
done
cd $path
