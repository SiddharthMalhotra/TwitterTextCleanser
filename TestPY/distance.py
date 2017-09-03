import Levenshtein

DictionaryTokens = open("OutlierTokens.txt","w")

def distance():
    with open("results.txt", "w") as result_file:
        with open("realtoken1.txt", "r") as token_file:
            for token in token_file:
                with open("dict.txt", "r") as dict_file:
                    for dic in dict_file:
                        if (Levenshtein.distance(token, dic) == 0):
                            result_file.write(token)

                            
if __name__ == '__main__':
    distance()
    
