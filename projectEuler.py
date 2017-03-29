primeList = [1,2,3,5,7,11,13,17,19]
extendedList = [4,8,9,12,16,18,20]


#iterates over primes less than twenty, dividing each time. Returns False if a number isn't divisible by a prime in list
def quick_factor_check(num):
	for prime in primeList:
		if num % prime != 0:
			return False

	return True		

def extended_factor_check(num):
	for factor in extendedList:
		if num % factor != 0:
			return False
	return True

def recursiveFactorial(num):
	if num == 1:
		return 1
	
	return num * recursiveFactorial(num-1)	

twentyFactorial = recursiveFactorial(20)

globalBeginningNum = 0
def smallestMultiple(beginningNum = 2520):
	print beginningNum
	endingNum = beginningNum + 1000000

	if beginningNum > twentyFactorial:
		return "You've made a huge mistake!"

	for number in range(beginningNum, endingNum):
		if quick_factor_check(number):
			if extended_factor_check(number):
				print str(number) + " is the number!!!!!"
				return
	globalBeginningNum = endingNum
	return smallestMultiple(endingNum)

try:
	smallestMultiple()
except:
	smallestMultiple(globalBeginningNum)


def increment(beginningNum = 10):
	print beginningNum
	if beginningNum > 500:
		return "Done!"
	return increment(beginningNum + 10)
