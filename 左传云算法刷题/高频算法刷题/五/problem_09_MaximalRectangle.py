# -*- encoding:utf-8 -*-


# Q:找出一个矩阵中，去最大矩形（1的个数）

# A:单调栈中遇到的一个数会被释放，该数的右边最近比该数小的
# A:该数在栈的底下，为左边最近比他小的数，若栈为空，则无

# 一个矩阵：
# 每次以某一行开始为底的矩阵，找出最大的矩阵
# 然后转化成一个数组，求出最大矩阵
# 以每一个元素开始扩
# 左边遇到高的能扩，右边比你高的也能扩，=>找出该元素，最近的比该元素小的

# 单调栈存在相等元素，单调栈中存放下标，相等也释放，表示向右扩不动，先计算，最终会有一个最后相等的元素尽心扩正确

class Stack():
	def __init__(self):
		self.array = []

	def push(self, item):
		self.array.append(item)

	def isEmpty(self):
		return len(self.array) == 0

	def pop(self):
		if self.isEmpty():
			return False
		return self.array.pop()

	def peek(self):
		if self.isEmpty():
			return False
		return self.array[-1]

	def size(self):
		return len(self.array)

class Solution:
	def maxRectangle(self, array):
		if not array or len(array) == 0 or len(array[0]) == 0:
			return 0
		maxarea = 0
		helpheight = [0 for i in range(len(array[0]))] # 记录每一行为底构造的数组
		for i in range(len(array)):
			for j in range(len(array[0])):
				helpheight[j] =  0 if array[i][j] == 0 else helpheight[j] + 1
			maxarea = max(maxarea, self.maxRecFromBottom(helpheight))
		return maxarea

	def maxRecFromBottom(self, array):
		if not array or len(array) == 0:
			return 0
		maxarea = 0
		stack = []
		for i in range(len(array)):
			while len(stack) != 0 and array[i] <= array[stack[-1]]:# 当前元素小于栈顶元素，开始弹出
				j = stack.pop()# 代表当前栈顶元素下标，进行计算

				k = -1 if len(stack) == 0 else stack[-1] # 代表左边界，若栈为空，则-1，否则当前栈顶
				curArea = array[j] * (i-k-1)
				maxarea = max(maxarea, curArea)
			stack.append(i)
		while len(stack) != 0:
			j = stack.pop()# 代表当前元素下标
			k = stack[-1] if len(stack) != 0 else -1 # 处理左边最小
			curArea = (len(array) - k - 1) * array[j]
			maxarea = max(maxarea, curArea)
		return maxarea
array = [[1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]
print(Solution().maxRectangle(array))
