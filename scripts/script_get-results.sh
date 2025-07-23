#!/bin/bash

# This scripts gets information from output PWSCF calculations.
###
# This script should run as ./script.sh <output_file> <results>
# where 'output_file' is the output PWSCF calculation, and 'results' is the resulted file
# after this script complets its job.
#
#
read -p "How many atoms there are in the system? " atoms
echo -e "############################################################\n" >> $2
echo -e "The system has $atoms atoms\n" >> $2
echo -e "============================================================\n" >> $2
echo -e "============================================================\n" >> $2
starts=`grep starts $1`
echo -e "It starts as: $starts" >> $2
echo -e "============================================================\n" >> $2
ends=`grep terminated $1`
echo -e "It ends as: $ends" >> $2
echo -e "============================================================\n" >> $2
procs=$(grep processor $1 | cut -d ',' -f 2 | awk '{print $3 " " "processors"}')
echo -e "The number of processors is $procs" >> $2
echo -e "============================================================\n" >> $2
time_spent=$(grep WALL $1 | tail -1 | cut -c 40- | cut -d ' ' -f 1-2)
echo -e "The program spent $time_spent" >> $2
echo -e "============================================================\n" >> $2
####################
####################
echo -e "\nChecking if the optimization has been fully performed in a relaxation calculation...\n" >> $2 
quest=$(grep " End of BFGS " $1)
if [[ $quest ]]
then
	echo -e "The calculation has been fully optimized." >> $2 
	echo -e "$quest in $(grep 'bfgs converged in' $1 | cut -d ' ' -f 10-)" >> $2
	echo -e "============================================================\n" >> $2
	echo -e "The final crystal parameters are:\n $(grep -A3 "CELL_PARAMETERS" $1 | tail -4)" >> $2
	echo -e "============================================================\n" >> $2
	echo -e "The final atomic positions (in angstroms) are:\n$(grep -A$atoms "ATOMIC_POSITIONS" $1 | tail -$atoms)" >> $2
	echo -e "============================================================\n" >> $2
	echo -e "Getting the scf results..." >> $2
	echo -e "============================================================\n" >> $2
	echo -e "The resulting forces (in Ry/au) on each of the $atoms atoms are:" >> $2
	echo -e "$(grep -A$(($atoms+1)) "Forces acting on atoms" $1 | tail -$atoms)\n" >> $2
	echo -e "The total stress per unit cell (in Ry/bohr**3) is:" >> $2
	echo -e "$(grep -A3 "Ry/bohr\*\*3" $1 | tail -3 | awk '{print $1 "  " $2 "  " $3}')\n" >> $2
	echo -e "The Pressure (in kbar) on the system is:" >> $2
	echo -e "$(grep "P= " $1 | tail -1 | cut -d ')' -f 3-)" >> $2
	echo -e "$(grep -A3 "P= " $1 | tail -3 | awk '{print $4 "   " $5 "   " $6}')\n" >> $2
	echo -e "The total energy is:" >> $2
	echo "$(grep ! $1 | tail -1 | awk '{print $5 " " $6}')" >> $2
	echo "or" >> $2
	echo -e "$(grep ! $1 | tail -1 | awk '{printf "%10.4f", $5*13.6057; print " " "eV"}')\n" >> $2
	echo -e "The calculated Fermi energy is:" >> $2
	echo -e "$(grep Fermi $1 | tail -1 | awk '{print $5 " " "eV"}')\n" >> $2
else
	echo -e "\nThis is not a optimization calculation, but rather a simple scf one.\n" >> $2
	echo -e "============================================================" >> $2
	echo -e "The total energy is:" >> $2
	echo "$(grep ! $1 | tail -1 | awk '{print $5 " " $6}')" >> $2
	echo "or" >> $2
	echo -e "$(grep ! $1 | tail -1 | awk '{printf "%10.4f", $5*13.6057; print " " "eV"}')\n" >> $2
	echo -e "The calculated Fermi energy is:" >> $2
	echo -e "$(grep Fermi $1 | tail -1 | awk '{print $5 " " "eV"}')\n" >> $2
fi
#########
#########
echo -e "\n============================================================" >> $2
echo -e "============================================================\n" >> $2
echo "Done!" >> $2
