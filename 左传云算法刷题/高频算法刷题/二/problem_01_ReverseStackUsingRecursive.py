# -*- encoding:utf-8 -*-

# Q: 递归反转一个栈
print("zjh")
class Stack():
	def __init__(self):
		self.array = []

	def push(self, item):
		self.array.append(item)

	def isEmpty(self):
		return len(self.array) == 0

	def pop(self):
		if  self.isEmpty():
			return False
		return self.array.pop()
	def peek(self):
		if self.isEmpty():
			return False
		return self.array[-1]

class Solution():
	def reverse(self, stack):
		if stack.isEmpty():
			return
		i = self.getAndRmoveLastElement(stack)
		self.reverse(stack)
		stack.push(i)

	def getAndRmoveLastElement(self, stack):
		result = stack.pop()
		if stack.isEmpty():
			return result
		else:
			last = self.getAndRmoveLastElement(stack)
			stack.push(result)
			return last

stack = Stack()
stack.push(1)
stack.push(2)
stack.push("zjh")
# print(stack)

while not stack:
	print(stack.pop())
Solution().reverse(stack)
while not stack.isEmpty:
	print(stack.pop())
	
