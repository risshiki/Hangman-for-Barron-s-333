import csv

wordlist = []

with open("wordsiknow.csv","r") as f:
    rf = csv.reader(f,delimiter = "\n")
    rf.readrow(wordlist)

print(wordlist)
