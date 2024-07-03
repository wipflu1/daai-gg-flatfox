#! /bin/bash
mkdir descriptions
cd descriptions

input_file="$1"
i =1
while IFS=',' read -r line; do
	echo "$line" >description_${1}.txt
	i++
done < "$input_file"

descriptions_list=(*.txt)
python3 sentimentAnalysis.py "${descriptions_list[@]}"
