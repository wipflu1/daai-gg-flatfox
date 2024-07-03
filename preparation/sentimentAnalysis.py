import sys

def sentimentAnalysis():
    with open(file_path, 'r') as file:
        data = file.read()
        #analysis


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("invalid number of arguments")
        sys.exit(1)
    for file_path in sys.argv[1:]:
        stringSentiment(file_path)
        

