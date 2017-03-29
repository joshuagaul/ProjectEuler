def sumNaturalSeries(maxValue):
	retSum = 0
	if maxValue % 2 == 0:
		retSum = (maxValue/2) *(maxValue + 1)
		return retSum
	elif maxValue % 2 != 0:
		return sumNaturalSeries(maxValue - 1) + maxValue

def squareSumNaturalSeries(maxValue):
	seriesSum = sumNaturalSeries(maxValue)
	return seriesSum ** 2

def squaresSeriesSum(maxValue):
	valuesList = map(lambda x: x **2, range(1,maxValue + 1))
	return reduce(lambda x,y: x+y, valuesList)

def squareAndSumDifference(maxValue):
	difference = squareSumNaturalSeries(maxValue)-squaresSeriesSum(maxValue)	
	return difference

