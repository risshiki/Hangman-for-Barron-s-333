import pickle
import csv

wordlist = []
worddict = {}

f = open("wordlist.txt",'r')

for line in f:
    definition = line.split('\t')
    definition[0] = definition[0].lower()
    wordlist.append(definition[0])
    worddict[definition[0]] = definition[1]

wordlist.sort()


with open("out.csv","w") as f:
    wr = csv.writer(f,delimiter="\n")
    wr.writerow(wordlist)


f.close()

