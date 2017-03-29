def numToWordLength(integer):
	numberWordDict = {0:"",1: "one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10: "ten", 11: "eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen", "three digit": "hundredand",20: "twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety","four digit":"thousand"}
	stringNum = str(integer)
	wordLiteral = ""

	wordLiteral = wordLiteral + numberWordDict[int(stringNum[len(stringNum) - 1])]

	if len(stringNum) >= 2:
		if int(stringNum[len(stringNum)-2:]) in numberWordDict:
			wordLiteral = numberWordDict[int(stringNum[len(stringNum)-2:])]
		else:
			wordLiteral = wordLiteral + numberWordDict[10*int(stringNum[len(stringNum)-2])]

	if len(stringNum ) == 3:
		wordLiteral = wordLiteral + numberWordDict[int(stringNum[len(stringNum)-3])]
		wordLiteral = wordLiteral + numberWordDict["three digit"]
	if len(stringNum) == 4:
		wordLiteral = wordLiteral + numberWordDict[int(stringNum[len(stringNum) - 4])]
		wordLiteral = wordLiteral + numberWordDict["four digit"]

	print wordLiteral
	if integer%100 == 0 and integer%1000 != 0:
		return len(wordLiteral) - 3
	return len(wordLiteral)

def finalAnswer():
	retNum = 0
	for num in range(1,1001):
		retNum = retNum + numToWordLength(num)
	return retNum