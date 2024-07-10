#! /bin/bash
mkdir descriptions

input_file="$1"								#first argument is input_file = descriptions csv file
IFS='!'
descr_pk=0								#initialize primary key for descriptions
data=$(<"$input_file")
for line in $data; do

	cd descriptions
	echo "$line" >descr_${descr_pk}.txt					#create new txt file for each entry of csv
	tr -d [:punct:] < descr_${descr_pk}.txt				#remove punctuation from each entry
	tr -d \[tn] < descr_${descr_pk}.txt
	echo description text file: "$descr_pk" created
	cd ..	
done < "$input_file"





#abhorent code that should almost certainly be ignored
#descriptions_list=(descr_100*)						#Create list of all txt files
#echo  calling sentiment analysis with : $1 ${descriptions_list[@]}
#python3 sentimentAnalysis.py "$1 ${descriptions_list[@]}"		#Call python script for analysis on all txt files
#
