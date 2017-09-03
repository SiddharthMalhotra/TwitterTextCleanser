import re

f=open("dict.txt",'r')
file=open("labelled-tokens.txt",'r')

with open('tokens.txt', 'w') as myFile:
	for line in file:
		sep = '\t'
		rest = line.split(sep, 1)[0] 
		myFile.write(rest)
		myFile.write('\n')

