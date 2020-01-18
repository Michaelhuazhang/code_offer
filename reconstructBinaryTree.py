# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 12:06 AM
# @Author  : Michael Zhang
# @Site    : 
# @File    : reconstructBinaryTree.py
# @Software: Sublime

'''
    利用二叉树前序遍历和中序遍历的特点，前序遍历的第一个值一定为根节点，对应
    中序遍历中间的一个点，，在中序遍历中，该点左侧的值为根节点的左子树，右侧的值
    为根节点的右子树。这时可以利用递归，取前序遍历的[1:i+1]和中序遍历的[:i]作为对应
    的左子树继续上一个过程，取前序遍历的[i+1:]和中序遍历的[i+1：]对应与右子树继续上一个guoc
    ，重建二叉树

'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# 返回构造的TreeNode 根节点
	def reConstructBinaryTree(self, pre, tin):
		# write code here
		if not pre and not tin:
			return None
		root = TreeNode(pre[0])
		# 建立根节点
		if set(pre) != set(tin):
			return None
		i = tin.index(pre[0])
		# 找到中序中的跟节点
		root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
		root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
		return root