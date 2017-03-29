
def primeListPop(maxValue):
	primeList = [2]
	for num in range(2, maxValue):
		primeFactorCounter = 0
		if num % 2 != 0:
			for prime in primeList:
				if num % prime == 0:
					primeFactorCounter = primeFactorCounter + 1
					break
					
			if primeFactorCounter == 0:
				primeList.append(num)
		if num % 10000 == 0:
			print num
	print primeList
	return primeList
	
def finalAnswer(maxValue):
	return reduce(lambda x,y: x + y, primeListPop(maxValue))
