# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 19:53 
# @Author  : Michael Zhang
# @Site    : 
# @File    : stack_prac
# @Software: PyCharm
'''
   利用两个栈实现一个队列，完成队列的Push和POP操作

   如果两个栈stack1和stack2 ，push的时候直接push进stack1
   POP需要判断stack1和stack2中的情况。如果stack2不为空的话
   直接从stack2中pop
   如果为空，把stack1中的值push到stack2中，然后再POP stack2中的值

'''
class Solution:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, node):
		self.stack1.append(node)
	def pop(self):
		if len(self.stack1) == 0 and len(self.stack2 == 0):
			return
		elif len(self.stack2) == 0:
			while len(self.stack1) > 0:
				self.stack2.append(self.stack1.pop())
		return self.stack2.pop()
