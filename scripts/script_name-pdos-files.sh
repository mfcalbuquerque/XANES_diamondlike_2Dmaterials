#!/bin/bash

cd $1_no-OH

for i in `ls atom$1.pdos.pdos_atm#$2\($3\)_wfc#*`
do mv ${i} ${i}.dat
done

ls -rt *.dat

cd ..

