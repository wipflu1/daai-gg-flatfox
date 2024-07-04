#! /bin/bash
mkdir descriptions
cd descriptions

input_file="$1"						#first argument is input_file = descriptions csv file
i =1
while IFS=',' read -r line; do
	echo "$line" >description_${i}.txt		#create new txt file for each entry of csv
	tr -d [:punt:] < description_${i}.txt		#remove punctuation from each entry
	i++
done < "$input_file"

descriptions_list=(description_[0-9]{0-10}.txt)			#Create list of all txt files
python3 sentimentAnalysis.py "$1 ${descriptions_list[@]}"	#Call python script for analysis on all txt files
rm description_[0-9]{0-10}.txt
