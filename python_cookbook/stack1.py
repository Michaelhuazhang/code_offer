#-*- encoding:utf-8 -*-

# class Stack:
# 	def __init__(self):
# 		self.item = []

# 	def push(self, item):
# 		self.item.append(item)

# 	def pop(self):
# 		return self.item.pop()

# 	def isEmpty(self):
# 		return self.item == []

# 	def size(self):
# 		return len(self.item)


# s1 = Stack()
# s1.push("ZJH")
# s1.push("26")
# print(s1.isEmpty())

# '''
# 字符串匹配
# '''
# def parChecker(symbolString):
# 	s = Stack()
# 	index = 0
# 	check = True
# 	while index < len(symbolString) and check:
# 		temp = symbolString[index]
# 		if temp == "(":
# 			s.push(temp)
# 		else:
# 			if s.isEmpty():
# 				check = False
# 			else:
# 				s.pop()
# 		index += 1
# 	if check and s.isEmpty():
# 		return True
# 	else:
# 		return False

# print(parChecker('((()))'))
# print(parChecker('(()'))


# '''
# 包括其他括号类型
# '''

# def matches(open, close):
# 	opens = ["(", "{", "["]
# 	closes = [")", "}", "]"]
# 	return opens.index(open) == closes.index(close)

# class Solution:
# 	def parChecker(self, strings):
# 		check = True
# 		index = 0
# 		s = Stack()
# 		while index < len(strings) and check:
# 			cur = strings[index]
# 			if cur in "{[(":
# 				s.push(cur)
# 			else:
# 				if s.isEmpty():
# 					check =  False
# 				else:
# 					top = s.pop()
# 					if not matches(top, cur):
# 						check = False
# 			index += 1
# 		if check and s.isEmpty():
# 			return True
# 		else:
# 			return False

# 	def matches(open, close):
# 		opens = ["(", "{", "["]
# 		closes = [")", "}", "]"]
# 		return opens.index(open) == closes.index(close)

# print("*" * 60)
# print(Solution().parChecker('{{([][])}()}'))
# print(Solution().parChecker('[{()]'))

# '''
# 进制之间的转换
# '''
# class Solution1:
# 	def baseConverter(self, decNumber, base):
# 		digits = "0123456789ABCDEF"
# 		temp_stack = Stack()
# 		while decNumber > 0:
# 			rem = decNumber % base
# 			temp_stack.push(rem)
# 			decNumber //= base

# 		final = ""
# 		while not temp_stack.isEmpty():
# 			final += digits[temp_stack.pop()]
# 		return final


# 	def infixToPostfix(self, infixexpr):
# 	    prec = {}
# 	    prec["*"] = 3
# 	    prec["/"] = 3
# 	    prec["+"] = 2
# 	    prec["-"] = 2
# 	    prec["("] = 1
# 	    opStack = Stack()
# 	    postfixList = []
# 	    tokenList = infixexpr.split()

# 	    for token in tokenList:
# 	        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
# 	            postfixList.append(token)
# 	        elif token == '(':
# 	            opStack.push(token)
# 	        elif token == ')':
# 	            topToken = opStack.pop()
# 	            while topToken != '(':
# 	                postfixList.append(topToken)
# 	                topToken = opStack.pop()
# 	        else:
# 	            while (not opStack.isEmpty()) and \
# 	               (prec[opStack.peek()] >= prec[token]):
# 	                  postfixList.append(opStack.pop())
# 	            opStack.push(token)

# 	    while not opStack.isEmpty():
# 	        postfixList.append(opStack.pop())
# 	    return " ".join(postfixList)

# print(Solution1().baseConverter(456, 16))


# def postfixEval(postfixExpr):
#     operandStack = Stack()
#     tokenList = postfixExpr.split()

#     for token in tokenList:
#         if token in "0123456789":
#             operandStack.push(int(token))
#         else:
#             operand2 = operandStack.pop()
#             operand1 = operandStack.pop()
#             result = doMath(token,operand1,operand2)
#             operandStack.push(result)
#     return operandStack.pop()

# def doMath(op, op1, op2):
#     if op == "*":
#         return op1 * op2
#     elif op == "/":
#         return op1 / op2
#     elif op == "+":
#         return op1 + op2
#     else:
#         return op1 - op2

# print(postfixEval('7 8 + 3 2 + /'))


class Solution2:
	def recMC(self, coinValueList, change):
		mincoins = change
		if change in coinValueList:
			return 1
		else:
			for i in [c for c in coinValueList if c <= change]:
				numcoins = 1 + self.recMC(coinValueList, change - i)
				if numcoins < mincoins:
					mincoins = numcoins
		return mincoins

	'''
      记住中间状态
	'''
	def recDC(self, coinValueList, change, knowResults):
		mincoins = change
		if change in coinValueList:
			knowResults[change] = 1
			return 1
		elif knowResults[change] > 0:
			return knowResults[change]
		else:
			for i in [c for c in coinValueList if c <= change]:
				numcoins = 1 + self.recDC(coinValueList, change - i, knowResults)
				if numcoins < mincoins:
					mincoins = numcoins
					knowResults[change] = mincoins
		return mincoins

# print(Solution2().recDC([1,5,10,25],63,[0]*64))

# print(Solution2().recMC([1, 5, 10, 25], 63))
print("ZJH")