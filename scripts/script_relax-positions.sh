#!/bin/bash

#This script has to be used when a relaxation calculation is stopped for some reason and you need to use the final positions in a new run (keep on relaxing the system).
#Beware: The card K_POINTS must be set after the card ATOMIC_POSITIONS for this script works well.
#
# This script should be run as: ./script <#_of_atoms> <last_output_file> <new_input_file>

read -p "Do you want to change atomic positions? Type y or any other letter. " q1

if [[ $q1 == y ]]
then
	line=`grep -n "ATOMIC_POSITIONS" $3 | cut -d ":" -f 1`
	line2=`grep -n "K_POINTS " $3 | cut -d ":" -f 1`

	grep -A$1 "ATOMIC_POSITIONS" $2 | tail -$1 >> file

	sed -i "$((${line}+1)),$((${line2}-1))d" $3 

	sed -i "${line}r file" $3

	rm file
else
	echo -e "Ok. Moving on.\n"
fi
##############################################
## Defining the SYSTEM card parameters. That means you will define a different Bravais lattice.
echo -e "\nNow, if you want to change the SYSTEM card parameters, just type 'y' for any of the following question."

read -p "Do you want to change the Bravais lattice and/or the CELL_PARAMETERS (for ibrav=0) card? y to proceed, or any other letter to exit? " q2
if [[ $q2 == y ]]
then
	echo -e "\nWhat is the new Bravais lattice code?"
	echo -e "You can choose the following ones:\n"
	echo -e "0 -- free crystal structure defined in the cell_parameters card"
	echo -e "1 -- simple cubic"
	echo -e "2 -- fcc"
	echo -e "4 -- hexagonal"
	echo -e "8 -- orthorrombic"
	echo -e "Among others. One can check in the user guide. But you will have to change the input by yourself.\n"
	read -p "Choose the one you want. " bravais
	if [ $bravais -eq 0 ]
	then
		sed -i "/.*ibrav.*/s/=.*/= $bravais,/" $3
		sed -i "/celldm(1)/d" $3
		sed -i "/celldm(3)/d" $3
		echo "CELL_PARAMETERS { alat }" > file2
		grep -A3 "CELL_PARAMETERS" $2 | tail -3 >> file2
		sed -i $'/ATOMIC_SPECIES/{e cat file2\n}' $3
		alat=`grep "CELL_PARAMETERS " $2 | tail -1 | cut -d "=" -f 2 | cut -d ")" -f 1`
		sed -i "/ibrav/a \     celldm(1) = ${alat}, " $3
	elif [ $bravais -eq 1 -o $bravais -eq 2 ]
	then
		sed -i "/celldm(2)/d" $3
		sed -i "/celldm(3)/d" $3
		sed -i "/celldm(1)/d" $3
		sed -i "/.*ibrav.*/s/=.*/= $bravais,/" $3
		alat=`grep "CELL_PARAMETERS " $2 | tail -1 | cut -d "=" -f 2 | cut -d ")" -f 1`
		sed -i "/ibrav/a \     celldm(1) = ${alat}, " $3
	elif [ $bravais -eq 4 ]
	then
		read -p "\nIf you have chosen code 4, then inform the size of the box in the z direction in Angstroms. " z
		sed -i "/celldm(2)/d" $3
		sed -i "/celldm(3)/d" $3
		sed -i "/celldm(1)/d" $3
		sed -i "/ibrav/s/=.*/= ${bravais},/" $3
		alat=`grep "CELL_PARAMETERS " $2 | tail -1 | cut -d "=" -f 2 | cut -d ")" -f 1`
		sed -i "/ibrav/a \     celldm(1) = ${alat}, " $3
		c=`echo "scale=4;$z / 0.5292 / $alat" | bc`
		sed -i "/celldm(1)/a \      celldm(3) = ${c}, " $3
	elif [ $bravais -eq 8 ]
	then
		echo -e "\nIf you have chosen code 8, you are going to inform the lattice parameters b and c in Angstroms."
	       	read -p "Inform the lattice parameter b. " b1
		read -p "Inform the lattice parameter c. " c1
		sed -i "/celldm(2)/d" $3
                sed -i "/celldm(3)/d" $3
                sed -i "/celldm(1)/d" $3
                sed -i "/ibrav/s/=.*/= ${bravais},/" $3
                alat=`grep "CELL_PARAMETERS " $2 | tail -1 | cut -d "=" -f 2 | cut -d ")" -f 1`
		sed -i "/ibrav/a \      celldm(1) = ${alat}, " $3
		balat=`echo "scale=4;$b1 / 0.5292 / $alat" | bc`
		sed -i "/celldm(1)/a \      celldm(2) = ${balat}, " $3
		calat=`echo "scale=4;$c1 / 0.5292 / $alat" | bc`
		sed -i "/celldm(2)/a \      celldm(3) = ${calat}, " $3
	else
		echo -e "\n==============================================================="
		echo "If you have chosen a different code, refer to the pw.x input variables on the QE website. Search for the ibrav variable."
		break
	fi
else
	echo -e "\nYou want to get the hell out of here. Ok... Bye!"
fi

rm file file2
echo -e "\n==============================================================="
echo "Done!"

