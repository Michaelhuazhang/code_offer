# -*- encoding:utf-8 -*-

class Stack:
	def __init__(self):
		self.array = []

	def push(self, data):
		self.array.append(data)

	def isEmpty(self):
		return len(self.array) == 0

	def pop(self):
		if self.isEmpty():
			return False
		return self.array.pop()

	def peek(self):
		if self.isEmpty():
			return None
		return self.array[-1]

		
class Solution:
	def maxRecSize(self, array):
		if not array or len(array) == 0 or len(array[0]) == 0:
			return 0
		# 记录最大矩形区域面积
		maxArea = 0
		# 辅助数组，记录每一行为底产生的最大矩形区域
		height = [0 for i in range(len(array[0]))]
		for i in range(len(array)):
			for j in range(len(array[0])):
				height[j] = 0 if array[i][j] == 0 else height[j] +1

			maxArea = max(maxArea, self.maxRecFromBottom(height))

		return maxArea

	def maxRecFromBottom(self, height):
		if not height or len(height) == 0:
			return 0
		maxArea = 0
		stack = Stack()
		for (i, num) in enumerate(height):
			while not stack.isEmpty() and num <= height[stack.peek()] :
				j = stack.pop()
				k = -1 if stack.isEmpty() else stack.peek()
				curArea = (i - k -1) * height[j]
				maxArea = max(curArea, maxArea)
			stack.push(i)
		while not stack.isEmpty():
			j = stack.pop()
			k = -1 if stack.isEmpty() else stack.pop()
			curArea = (len(height)- k -1) * height[j]
			maxArea = max(maxArea, curArea)
		return maxArea

array = [[1, 0, 1, 1], [ 1, 1, 1, 1], [ 1, 1, 1, 0 ]]
print(Solution().maxRecSize(array))


