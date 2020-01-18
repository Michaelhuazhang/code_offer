# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 16:53
# @Author  : Michael Zhang
# @Site    : 
# @File    : PrintMatrix.py
# @Software: Sublime

'''
Q: 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，

A: 首先，判断每一圈开始的坐标点，是否小于行数的一半且小于列数的一半。打印
'''

class Solution:
	def printMatrix(self, matrix):
		if not matrix:
			return []
		rows = len(matrix)
		columns = len(matrix[0])

		start = 0
		result = []

		while rows > start * 2 and columns > start * 2:
			self.PrintMatrixInCricle(matrix, columns, rows, start, result)
			start += 1
		return result

	def PrintMatrixInCricle(self, matrix, columns, rows, start, result):
		endX = columns - 1 - start
		endY = rows - 1 - start
		# 从左往右打印一行
		for i in range(start, endX+1):
			result.append(matrix[start][i])
		# 从上往下打印一列
		if start < endY:
			for i in range(start+1, endY +1):
				result.append(matrix[i][endX])
		# 从右往左打印
		if start < endX and start < endY:
			for i in range(endX-1, start-1, -1):
				result.append(matrix[endY][i])
		# 从下往上打印
		if start < endX and start< endY - 1:
			for i in range(endY-1, start, -1):
				result.append(matrix[i][start])

print(Solution().printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))