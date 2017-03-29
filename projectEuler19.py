monthList= [31,28,31,30,31,30,31,31,30,31,30,31]
sundayCounter = 0
monthCounter =
year = 1901

def sundayCheck(daysSinceBeg):
	if daysSinceBeg % 7 == 1:
		return True
	else:
		return False

def finalAnswer(years):
	daysSinceBeg = 0
	for n in range(years*12):
		daysSinceBeg = daysSinceBeg + monthList[n%12]


