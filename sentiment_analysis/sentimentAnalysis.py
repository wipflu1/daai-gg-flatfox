import sys
import csv
def sentimentAnalysis():
    totalSentiment=0                                        #total sentiment value of the txt file
    with open(file_path, 'r') as file:                      #open txt file
        data = file.read()                                  #data = text within txt file
        words =  data.split()                               #words = list of words within data
        for word in words:                                  #itterate words 
            with open('sentiment.csv', 'rt') as file:       #assume sentiment.csv = csv of swiss words
                reader = csv.reader(file, delimeter=',')    #copied from stackoverflow
                for row in reader:                          #^
                    if word == row[0]:                      #assuming row[0] = word
                        totalSentiment+=row[1]              # assuming row[1] = word's sentiment value

if __name__ == "__main__":                                  #if called from sh script??
    if len(sys.argv) < 2:                                   #error if less than 1 arguement
        print("invalid number of arguments")                
        sys.exit(1)
    for file_path in sys.argv[1:]:                          #call sentimentAnalysis for every arguement provided
        sentimentAnalysis(file_path)
        

