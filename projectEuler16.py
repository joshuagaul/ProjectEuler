def digitSum(number):
	numString = str(number)
	summation = 0
	for letter in numString:
		summation = summation + int(letter)
	return summation

def finalAnswer():
	return digitSum(2**1000)