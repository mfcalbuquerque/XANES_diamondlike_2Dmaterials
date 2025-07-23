#!/bin/bash

#This script gathers the values from a proj.dat file output from a projwfc.x (with no symmetry) calculations.
#The newly-generated files have to be used in the plotband.x to get a band structure file with projections (a three-columns file).

#It should be run as: ./script <proj.dat> (projwfc.x output)

echo "Pz states."
grep " 2    1    1" $1 | awk '{print $1}' | awk 'BEGIN{ORS=" "}{print}' 
echo ""
echo "Px states."
grep " 2    1    2" $1 | awk '{print $1}' | awk 'BEGIN{ORS=" "}{print}'
echo ""
#echo "Py states."
#grep " 2    1    3" $1 | awk '{print $1}' | awk 'BEGIN{ORS=" "}{print}'
#echo ""
echo "S states."
grep " 1    0    1" $1 | awk '{print $1}' | awk 'BEGIN{ORS=" "}{print}'

#########################################################################
#echo "The contribution for the nearest atoms, including the absorbing one."
#### Change this values if you wish other atoms.
#for i in 38C 37C 45C 69C
#do
#	grep " $i" $1
#done
