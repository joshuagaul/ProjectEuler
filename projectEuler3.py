def factorize(num):
	retList = []
	for possibleFactor in range(1,int(num**.5)):
		if num % possibleFactor == 0:
			#print str(possibleFactor) + " is a factor and " + str(num/possibleFactor) + " is a factor"
			retList.append(possibleFactor)
			retList.append(num/possibleFactor)
	retList.sort()	
	return retList

def primeFactorize(numList):
	retList = []
	for num in range(len(numList) - 1 ):
		factors = factorize(numList[num])
		if len(factors) > 2:
			retList.append(primeFactorize(factors))
		elif len(factors) <= 2:
			retList.append(numList[num])

	return retList		 

def findBiggest(numList):
	biggest = 0
	for num in numList:
		if type(num) == list:
			bigInList = findBiggest(num)
			if bigInList > biggest:
				biggest = bigInList
		elif num > biggest:
			biggest = num

	return biggest

l = factorize(600851475143)
l2 = primeFactorize(l);
print str(findBiggest(l2))