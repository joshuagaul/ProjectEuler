primesList = [2]

def primeCheck(num):
	if num not in primesList:
		if len(filter(lambda x: num % x == 0, primesList)) == 0:
			return True
	return False

globalBeginningNum = 0
def findPrimeAtPosition(position,beginningNum = 2,endingNum = 10000000 ):
	for num in range(beginningNum,endingNum):
		if len(primesList) == position:
			print str(primesList[len(primesList) -1]) + " is the number " + str(position) + " prime" 
			return	
		elif primeCheck(num):
			primesList.append(num)
			print "Appending "	+ str(num) + "\t " + str(len(primesList))
		else:
			print num

	globalBeginningNum = endingNum

	return findPrimeAtPosition(position, endingNum, endingNum + endingNum)

