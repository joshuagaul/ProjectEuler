def palindromeCheck(integer):
	firstHalf = ""
	secondHalf = ""
	if len(str(integer)) % 2 != 0:
		#print "odd amount of digits"
		firstHalf = str(integer)[0: len(str(integer))//2]
		secondHalf = str(integer)[len(firstHalf) + 1 : len(str(integer))]
	elif len(str(integer))%2 == 0:
		#print "even amount of digits"
		firstHalf = str(integer)[0:len(str(integer))/2]
		secondHalf = str(integer)[len(str(integer))/2 : len(str(integer))]
	#print firstHalf
	#print secondHalf
	if firstHalf == secondHalf[::-1]:
		return True
	else:
		return False

def finalAnswer():
	palindromeList = []
	counter = 100
	for num1 in range(100,1001):
		for num2 in range(counter, 1001):
			#print str(num1) + ": " + str(num2)
			if palindromeCheck(num1*num2):
				palindromeList.append(num1*num2)
		counter = counter + 1
		#print num1, num2
	palindromeList.sort()
	return palindromeList[len(palindromeList) - 1]

fa = finalAnswer()
print str(fa)

