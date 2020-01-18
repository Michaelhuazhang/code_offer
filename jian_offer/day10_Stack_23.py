
'''
Q: 包含栈的数据结构，请在该类型实现一个能够得到栈中最小元素的min函数

A:建立一个辅助栈，每次进栈的同时，将最小值压入辅助栈，这样辅助栈的栈顶一直是最小元素。当数据栈中，最小值
被弹出时，同时弹出辅助栈的栈顶元素

'''
class Solution:
	def __init__(self):
		self.stack = []
		self.minStack = []

	def push(self, node):
		self.stack.append(node)
		# 将最小值入栈
		if self.minStack == [] or node < self.min():
			self.minStack.append(node)
		else:
			temp =self.min() # 找到当前最小的入最小栈
			self.minStack.append(temp)

	def pop(self):
		if self.stack == None or self.minStack == None:
			return None
		self.minStack.pop()
		self.stack.pop()
	def top(self):
		return self.stack[-1]
	def min(self):
		return self.minStack[-1]