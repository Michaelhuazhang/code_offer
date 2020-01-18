# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 19:59
# @Author  : Michael Zhang
# @Site    : 
# @File    : day5_reconstruct_binayTree.py
# @Software: Sublime


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def reconstruct_binaryTree(self, pre, tin):
		if not pre and not tin:
			return None
		root = TreeNode(pre[0])
		if set(pre) != set(tin):
			return None
		i = tin.index(pre[0])

		root.left = self.reconstruct_binaryTree(pre[1:i+1], tin[:i])
		root.right = self.reconstruct_binaryTree(pre[i+1:], tin[i+1:])
		return root
		