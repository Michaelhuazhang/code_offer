# -*- encoding:utf-8 -*-
# 合并两颗树
# 遇到树问题，首先想到递归
# 将t2的val加到t1，返回当前处理的t1结点
# 如果t1为null，把引用指向t2
# 需要注意处理null的问题

class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def mergeTwoTree(self, t1, t2):
		if  t1 and  t2:
			t1.val += t2.val
			tl.left = self.mergeTwoTree(t1.left, t2.left)
			t1.right = self.mergeTwoTree(t1.right, t2.right)
		elif not t1 and t2:
			t1 = t2
		return t1
