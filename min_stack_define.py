# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 16:53
# @Author  : Michael Zhang
# @Site    : 
# @File    : min_stack.py
# @Software: Sublime

'''
Q: 定义栈的数据结构，请在该类型当中实现一个能够得到栈中所含最小元素的min函数


A:建立一个辅助栈，每次豆浆最小值压入辅助栈，这样辅助栈的栈顶一直都是最小元素，当数据栈中，最小值被弹出来时，同时弹出辅助栈的栈顶元素

'''

class Solution:
	def __init__(self):
		self.stack = []
		self.minStack = []
	def push(self, node):
		self.stack.append(node)
		# 如果当前元素小于辅助栈顶元素或者辅助栈为空，在辅助栈中压入元素
		if self.minStack == [] or node < self.min():
			self.minStack.append(node)
		else:
			temp = self.min() # 辅助栈中依旧是之前的元素，保持辅助栈中一直是最小
			self.minStack.append(temp)
	def pop(self):
		if self.stack == None or self.minStack == None:
			return None
		self.minStack.pop()
		self.stack.pop()

	def top(self):
		return self.stack[-1]
	def min(self):
		return minStack[-1]
		
