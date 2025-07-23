#!/bin/bash

### This script reads files and changes its content accordingly as explained below.
### It should be run as: ./script (see below!)
###
### NOTE: You should define the variable according to the files you want to change.
### For example: file=$(ls *.in) will get all the file names ending with '.in' in this directory.

#xxx=$1
#for index in `seq 1 $xxx`
#do
#	for index2 `ls $2`
#	do
#		file[$index]=$index2
#	done
#done

file=`ls *.in`

echo -e "You are going to choose the number of lines to change.\nIf you want to change the k-points sampling, then do not consider that line in the following question.\nIt would be requested soon.\n"
read -p 'Inform how many lines you wish to replace: ' n
echo -e "$n lines will be changed."
#################
if [ $n -eq 0 ]
then
	read -p "Do you want to change k-points sampling in your input files? y or n?" question
	if [ $question == y ]
	then
		read -p "Inform the old sampling (kx ky kz): " old_sampling
		read -p "Inform the new sampling (kx ky kz): " new_sampling
		sed -i "/$old_sampling/s/$old_sampling/$new_sampling/" $file
		exit
	else
		echo -e "\nOkay! Now, you can proceed with your work."
	fi
fi
#################
echo -e "\n================================================== \n"
### Please inform the line(s) of the file you want to replace, according to the number of lines you have typed.
# content = the word the the line n contains
# new_word = the word that you are willing see after the changing
for i in `seq 1 $n`
do
	read -p "Inform the content of the line number $i, so that you can alter it: " content
	read -p "Inform which word it will be replaced with: " new_word  #### If it has '/', or other special sign, it must be defined as \\/xxx
	### Loop over the desired files to perform the desired changes
	for j in $file
	do
		test='^[0-9]+$'
		if [[ $new_word =~ $test ]]
		then
			sed -i "/$content/s/= .*,/= $new_word,/" $j   ### It changes numerical values.
		else
			sed -i "/$content/s/'.*'/'$new_word'/" $j     ### It changes string variables, which are sorrounded by ""
		fi
		
	done
done

### Changing k-points sampling

read -p "Do you want to change k-points sampling in your input files? y or n?" question

if [ $question == y ]
then
	read -p "Inform the old sampling (kx ky kz): " old_sampling
	read -p "Inform the new sampling (kx ky kz): " new_sampling
	sed -i "/$old_sampling/s/$old_sampling/$new_sampling/" $file
else
	echo -e "\nOkay! Now, you can proceed with your work."
fi
echo -e "\n================================================== \n"
echo "Done!"
