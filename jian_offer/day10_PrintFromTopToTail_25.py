'''
从上往下打印
A: 引入一个队列，每次打印一个，如果该节点有子节点，则进队
'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def PrintFromTopToBottom(self, root):
		if root is None:
			return []
		queue = []
		result = []
		queue.append(root)
		while len(queue):
			currentRoot = queue.pop(0)
			result.append(currentRoot.val)

			if currentRoot.left:
				queue.append(currentRoot.left)
			if currentRoot.right:
				queue.append(currentRoot.right)
		return result
		