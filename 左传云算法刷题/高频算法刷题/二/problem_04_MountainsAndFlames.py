# -*- encoding:utf-8 -*-
# 看到对面上峰，我需要找到两侧比它大的数
# 单调栈可以实现这种数据结构
# 单调栈：栈顶从大到小
# 1、找到最大的一个元素，开始进栈（记录次数）
# 2、开始构造




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

# stack = Stack()
# stack.push(1)
# stack.push(23)
# stack.push(456)
# while not stack.isEmpty():
# 	print(stack.pop())
# 单调栈中记录的类型
class Pair():
	def __init__(self, value):
		self.value = value
		self.times = 1


class Solution():
	def nextIndex(self, size, i):
		return i + 1 if i < size - 1 else 0

	def getInternalSum(self, n):
		# Cn2
		return 0 if n == 1 else n * (n-1) / 2

	def communication(self, array):
		if not array or len(array) < 2:
			return 0
		size = len(array)
		maxIndex = 0
		for i in range(len(array)):
			maxIndex = i if array[i] < array[maxIndex] else maxIndex

		value = array[maxIndex]
		index = self.nextIndex(size, maxIndex)
		res = 0
		stack = Stack()
		stack.push(Pair(value))
		while index != maxIndex:
			value = array[index]
			while not stack.isEmpty() and stack.peek().value < value:
				times = stack.pop().times
				res += self.getInternalSum(times) + 2 * times

			if (not stack.isEmpty() and stack.peek().value == value):
				stack.peek().times += 1
			else:
				stack.push(Pair(value))
			index = self.nextIndex(size, index)

		# 结算栈中剩余元素
		while not stack.isEmpty():
			times = stack.pop().times
			res += self.getInternalSum(times)
			if not stack.isEmpty():
				res += times # 当前栈顶
				if stack.size() > 1:
					res += times
				else:
					res += times if stack.peek().times > 1 else 0
		return res


print(Solution().communication([4, 1, 2, 3, 5, 7, 6, 9, 2, 5]))



