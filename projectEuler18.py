class pascalTriangle:
	def __init__(self,rows):
		self.rows = rows
		self.arrayRepresentation = []
		rowPop()

	def rowPop():
		for row in range(self.rows):
			self.arrayRepresentation.append([[]])

		for row in range(self.rows):
			for column in range(row + 1):
				if row == 0 or row == 1:
					self.arrayRepresentation[row][column] = 1