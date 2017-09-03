file1 = "OutlierTokens.txt"
file2 = "tokens.txt"
file3 = open("nonmatches.txt",'w')

with open(file1,'rU') as f:
    t1 = f.read().splitlines()
    t1s = set(t1)

with open(file2,'rU') as f:
    t2 = f.read().splitlines()
    t2s = set(t2)

#in file2 but not file1
for diff in t2s-t1s:
	file3.write(diff)
	file3.write("\n")
