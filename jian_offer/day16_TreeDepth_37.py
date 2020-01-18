

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def TreeDepth(self, pRoot):
		'''
            当前树的深度（左子树的深度和右子树的深度最大 +1）

		'''
		if not pRoot:
			return 0
		return max(self.TreeDepth(pRoot.left) , self.TreeDepth(pRoot.right)) + 1

	def Isbalanced_solution(self, pRoot):
		'''
           |左子树的深度 -右子树的深度| <= 1
		'''
		if not pRoot:
			return True
		highl = self.TreeDepth(pRoot.left)
		highr = self.TreeDepth(pRoot.right)
		if abs(highr - highl) > 1:
			return False

		return True

	def __init__(self):
		self.flag = True
		
	def Isbalanced_solution_1(self, pRoot):
		self.getDepth(pRoot)
		return self.flag

	def getDepth(self, pRoot):
		if not pRoot:
			return 0
		left = self.getDepth(pRoot.left) + 1
		right = self.getDepth(pRoot.right) + 1
		if abs(left - right) > 1:
			self.flag = False