# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 20:31
# @Author  : Michael Zhang
# @Site    : 
# @File    : day5_stacktoqueue_9.py
# @Software: Sublime
'''
插入的时候直接插
删除的时候，先把stack1进，若stack2空的话
将stack1进栈，不空的话，先进先出，没有问题，始终是栈2进行弹出的操作

'''
class Solution:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, node):
		self.stack1.append(node)

	def pop(self):
		if len(self.stack1) == 0 and len(self.stack2) == 0:
			return
		elif len(self.stack2) == 0:
			while len(stack1) > 0:
				self.stack2.append(self.stack1.pop())
			
		return self.stack2.pop()

		