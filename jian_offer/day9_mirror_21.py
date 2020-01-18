'''
操作给定的二叉树，将其变换为元二叉树的镜像


A:先前序遍历树的每个节点，如果遍历到树的结点有子节点，则交换
交换完所有的非叶子节点，得到树的镜像
'''
class Solution:
	def Mirror(self, root):
		if root == None:
			return
		if root.left == None and root.right == None:
			return root

		ptemp = root.left
		root.left = root.right
		root.right = ptemp
		## 交换根节点的左右节点
		# 交换所有的子节点
		self.Mirror(root.left)
		self.Mirror(root.right)
		# 递归前序遍历