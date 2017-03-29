def pyTripletCheck(triplet):
	print "Checking " + str(triplet[0]) + "\t" + str(triplet[1]) + "\t" + str(triplet[2])
	pySum = (triplet[0]**2) + (triplet[1]**2)
	if pySum == (triplet[2]**2):
		return True
	else:
		return False	

def listPerm(maxValue):
	retList = []
	seriesSum = 0
	endingPoint = maxValue
	for num1 in range(1,endingPoint):
		num2EndingPoint = endingPoint - num1
		for num2 in range(1,maxValue):
			num3 = maxValue - num1 - num2
			if num3 > 0 and num3 > num1 and num3>num2 and ((num1**2) + (num2**2)>num3) and (num2 + num1)> num3:
				series = []
				series.append(num1)
				series.append(num2)
				series.append(num3)

				if series not in retList:
					retList.append(series)
					print "Appending " + str(num1) + " " + str(num2) + " " + str(num3)		

	return retList					

def finalAnswer():
	return filter(lambda x: pyTripletCheck(x), listPerm(1000))

