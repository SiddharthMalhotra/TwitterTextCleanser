import re
file=open('tokens.txt', 'rU')

text_file = open("results.txt", "a")
OutlierTokens = open("OutlierTokens.txt","w")

for line in file:
    if((line[:1])=='@'):
    	text_file.write(line+'\t'+'NO'+'\t'+line)
    	OutlierTokens.write(line)
    if((line[:1])=='#'):
    	text_file.write(line+'\t'+'NO'+'\t'+line)
    	OutlierTokens.write(line)
    if((line[:1])=='!'):
    	text_file.write(line+'\t'+'NO'+'\t'+line)
    	OutlierTokens.write(line)
    if((line[:4])=='http'):
    	text_file.write(line+'\t'+'NO'+'\t'+line)
    	OutlierTokens.write(line)
    	
