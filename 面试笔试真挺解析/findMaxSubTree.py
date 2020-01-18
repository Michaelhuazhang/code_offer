# -*- encoding:utf-8 -*-

'''
Q: 如何求一个二叉树的最大子树和

A: 一个子树的和为左子树的和+右子树的和+根
二叉树的最大子树和，最容易想的就是针对每颗子树，求出每颗子树所有结点的和
从中找到最大值

'''
class TreeNode():
	"""docstring for TreeNode"""
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Solution:
	def __init__(self):
		self.maxSum = -2**31
	def findMaxSubTree(self, root):
		if not root:
			return 0
		leftmax = self.findMaxSubTree(root.left)
		rightmax = self.findMaxSubTree(root.right)
		sums = root.data + leftmax + rightmax
		if sums > self.maxSum:
			self.maxSum = sums
			maxRoot = TreeNode()
			maxRoot.data = root.data
		return sums
	def isEqual(self, root1, root2):
		if not root1 and not root2:
			return True
		if not root1 and root2:
			return False
		if root1 and not root2:
			return False
		if root1.data == root2.data:
			return self.isEqual(root1.left, root2.left) and self.isEqual(root1.right) and self.isEqual(root2.right)
	
	def arraytoTree(self, array, start, end):
		if end >= start:
			mid = (end + start + 1) / 2
			root = TreeNode(array[mid])
			root.left = self.arraytoTree(array, start, mid-1)
			root.right = self.arraytoTree(array, mid + 1, end)
		else:
			root = None
		return root

	### 求两个节点的距离
	# 两个节点的距离等于，根到两个节点的距离 - 2倍的根到父节点的距离
	def getParendNode(self, root, node1, node2):
		if not root or root == node2 or root == node1:
			return root
		left = self.getParendNode(root.left, node1, node2)
		right = self.getParendNode(root.right, node1, node2)
		if not left:
			return right
		elif not right:
			return left
		else:
			return root

	def getDistanceNode(self, start, end):
		if not start or not end or start == end:
			return 0
		queue = []
		level = 0
		queue.append(start)
		while queue:
			temp = queue.pop(0)

			if temp.left:
				queue.append(temp.left)
				level += 1
				if temp.left == end:
					return level

			if temp.right:
				queue.append(temp.right)
				if  not temp.left:
					level += 1
				if temp.right == end:
					return level
	def getDistance(self,root, node1, node2):
		parent = self.getParendNode(root, node1, node2)
		return self.getDistanceNode(root, node1) + self.getDistanceNode(root, node2) - 2 * self.getDistanceNode(root, parent)

		



