def main():
	filename = 'Nresult.txt'
	highestsum = 0.0
	count = [0,0,0,0,0]
	with open(filename, 'rU') as token_file:
		for token in token_file:
			print token
			if token == 'N=1\n':
				count[0] = count[0] + 1
			elif token == 'N=2\n':
				count[1] += 1
			elif token == 'N=3\n':
				count[2] += 1
			elif token == 'N=4\n':
				count[3] += 1
			elif token == 'N=5\n':
				count[4] += 1
	for i in range(0,5):
		print count[i] 


main()
