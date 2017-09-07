import csv

f = open("wordlist.txt",'r')

worddict = {}
for line in f:
    definition = line.split('\t')
    definition[0] = definition[0].lower()
    worddict[definition[0]] = definition[1]

dkwords = []
with open("wordsiknow.csv",'r') as f:
    for line in f:
        definition = line.split(',')
        definition[1] = definition[1].strip()
        if 'a' in definition[1]:
            dkwords.append(definition[0])

f.close()

f = open("notlearntwords.txt",'w')

for word in dkwords:
    appendline = word + "\t" + worddict[word]
    f.write(appendline)

f.close()

