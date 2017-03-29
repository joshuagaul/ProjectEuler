def iFactorial(number):
	if number == 0 or number == 1:
		return 1
	return reduce(lambda x,y: x*y, range(1,number+1))

def finalAnswer(x,y):
	numerator = iFactorial(x+x)
	denominator = iFactorial(y)*(iFactorial(x))
	return numerator/denominator








	 