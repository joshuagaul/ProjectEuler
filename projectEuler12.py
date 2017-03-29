def factorize(num):
	retList = []
	for possibleFactor in range(1,int(num**.5)):
		if num % possibleFactor == 0:
			#print str(possibleFactor) + " is a factor and " + str(num/possibleFactor) + " is a factor"
			retList.append(possibleFactor)
			retList.append(num/possibleFactor)
	retList.sort()	
	return retList

def triangularNumbers(nthPosition):
	retNumber = 0
	if nthPosition % 2 != 0:
		retNumber = retNumber + nthPosition + triangularNumbers(nthPosition - 1)
	else:
		retNumber = (retNumber + nthPosition + 1)*(nthPosition/2)
	return retNumber

def finalAnswer():
	counter = 1
	while True:
		triangularNumber = triangularNumbers(counter)
		print triangularNumber
		if triangularNumber > 500:
			if len(factorize(triangularNumber)) > 500:
				return triangularNumber
		counter = counter + 1
