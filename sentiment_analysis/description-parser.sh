#! /bin/bash
mkdir descriptions

input_file="$1"						#first argument is input_file = descriptions csv file
i=1
while IFS=',' read -r line; do
	cd descriptions
	echo "$line" >description_text_num_${i}.txt		#create new txt file for each entry of csv
	tr -d [:punct:] < description_text_num_${i}.txt		#remove punctuation from each entry
	tr -d \[tn] < description_text_num_${i}.txt
	i=$((i+1))
	echo description text file: "$i" created
	cd ..	
done < "$input_file"

descriptions_list=(description_text_num_*)			#Create list of all txt files
echo  calling sentiment analysis with : $1 ${descriptions_list[@]}
python3 ../sentimentAnalysis.py "$1 ${descriptions_list[@]}"	#Call python script for analysis on all txt files
rm description_text_num_*
