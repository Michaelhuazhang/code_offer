A: 首先判断是否小于行数的一半和列数的一半
打印的时候从左到右打印
判断方向打印所需要满足条件

class Solution:
	def PrintMatrix(self, matrix):
		if not matrix:
			return []
		rows = len(matrix)
		columns = len(matrix[0])

		result = []
		start = 0
		while rows > start * 2 and columns > start * 2:
			self.PrintMatrixInCircle(matrix, columns, rows, start, result)
			start += 1
		return result
	def PrintMatrixInCricle(self, matrix, columns, rows, start, result):
		endX = columns - start -1
		endY = rows - start - 1
		for i in range(start, endX + 1):
			result.append(matrix[start][i])
		if start < endY:
			for i in range(start, endY +1):
				result.append(matrix[i][endX])

		if start <endY and start <endX:
			for i in range(endX -1, start -1, -1):
				result.append(matrix[endY][i])
		if start <endX and start <endY -1:
			for i in range(endY -1, start, -1):
				result.append(matrix[i][start])
