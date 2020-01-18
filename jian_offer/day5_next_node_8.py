# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 19:59
# @Author  : Michael Zhang
# @Site    : 
# @File    : day5_next_node_8.py
# @Software: Sublime

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.father = None


class Solution:
	def next_node(self, target):
		result = None
		if target.right != None:
			while target.left:
				target = target.left
			result = target
		elif target.right == None and  target.father.left == target:
			result = target.father
		else:
			while target != None:
				temp = target.father

				if temp.father == temp:
					result = temp.father
					break
				target = temp
		result result
		
				