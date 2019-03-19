from functools import reduce
import sys



def power_digits(power, digit_list):
	if (power == 0):
		return digit_list

	plus_one = False

	for i in range(len(digit_list) - 1, -1, -1):
		result = digit_list[i] * 2

		if result >= 10:
			if plus_one:
				digit_list[i] = result - 10 + 1
			else:
				digit_list[i] = result - 10

			plus_one = True
		
		else:
			if plus_one:
				digit_list[i] = result + 1
			else:
				digit_list[i] = result

			plus_one = False
		
	if (plus_one):
			digit_list.insert(0, 1)

	return power_digits(power - 1, digit_list)


if __name__ == '__main__':
	assert power_digits(1, [1]) == [2]

	assert power_digits(2, [1]) == [4]
	assert power_digits(3, [1]) == [8]

	assert power_digits(4, [1]) == [1,6]
	assert power_digits(5, [1]) == [3,2]

	sys.setrecursionlimit(1500)
	print(power_digits(1000, [1]))
	print(reduce(lambda x, y: x + y, power_digits(1000, [1])))



			


