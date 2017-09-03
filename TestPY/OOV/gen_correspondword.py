import ngram
def main():

	resultname = 'Correspond.txt'
	file = open(resultname,'w') 
	filename = 'realtoken1.txt'
	highestsum = 0.0
	with open(filename, 'rU') as token_file:
		for token in token_file:
			highest = 0.0
			candidate = '';
			with open("dict.txt", 'rU') as dict_file:
				value = 0.0
				for dic in dict_file:
					value = ngram.NGram.compare(token,dic,N=1)
					if highest < value:
						highest = value
						candidate = dic
			file.write(candidate)


main()