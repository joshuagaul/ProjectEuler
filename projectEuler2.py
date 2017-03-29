def iFib(maxValue):
	fibList = [1,1]
	fibValue = 0
	counter = 2
	while fibValue < maxValue:
		fibValue = fibList[counter -1] + fibList[counter - 2]
		fibList.append(fibValue)
		counter = counter + 1
	if fibList[len(fibList) - 1] > maxValue:
		fibList.remove(fibList[len(fibList )-1])
	return fibList	

def finalAnswer(maxValue):
	evenFib = filter(lambda x: x%2 == 0, iFib(maxValue))
	return reduce(lambda x,y: x+y, evenFib)	