def collatzGen(begNum):
	retList = [begNum] 
	go = True
	while go:
		if retList[len(retList)-1] % 2 == 0:
			retList.append(retList[len(retList)-1]/2)
		else:
			retList.append(3*retList[len(retList)-1] + 1)

		if retList[len(retList)-1] == 1:
			go = False

	return retList

def finalAnswer(maxValue):
	biggest = 0
	startingNumber = 0
	for num in range(1 , maxValue + 1):
		collatzSeries = collatzGen(num)
		if len(collatzSeries) > biggest:
			startingNumber = num
			biggest = len(collatzSeries)
		if num % 10000 == 0:
			print num, startingNumber, biggest
	return startingNumber