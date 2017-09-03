file1 = open('DictionaryTokens.txt').readlines()
file2 = open('OutlierTokens.txt').readlines()
with open('LeftOverWords.txt', 'w') as result:
    for line in open('tokens.txt'):
        if line not in file2 and line not in file1:
            result.write(line)