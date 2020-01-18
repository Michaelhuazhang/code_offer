# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 17:01
# @Author  : Michael Zhang
# @Site    : 
# @File    : HasSubTree.py
# @Software: Sublime

'''
Q: 输入两棵二叉树A，B，判断B是不是A的子结构



A:在树A中查找和树B根节点一直的值，然后判断A中以该节点为根节点的子树，是不是和B有相同的结构，可以通过递归实现
'''

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def HasSubTree(self, pRoot1, pRoot2):
		result = False
		if pRoot1 != None and pRoot2 != None:
			if pRoot1.val == pRoot2.val:
				result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
			if not result:
				result = self.DoesTree1HaveTree2(pRoot1.left, pRoot2)
			if not result:
				result = self.DoesTree1HaveTree2(pRoot1.right, pRoot2)
		return result

	def DoesTree1HaveTree2(self, pRoot1, pRoot2):
		if pRoot2 == None:
			return True
		if pRoot1 == None:
			return False
		if pRoot1.val != pRoot2.val:
			return False
		return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)
		
