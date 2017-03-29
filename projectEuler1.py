

def listPop(maxValue):
	multiples = []
	for num in range(1,maxValue):
		if num % 5 == 0:
			multiples.append(num)
		elif num % 3 == 0:
			multiples.append(num)
	return multiples

def finalAnswer(maxValue):
	return reduce(lambda x,y: x+y, listPop(maxValue)) 

