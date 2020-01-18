'''
输入一棵二叉搜索树，
将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，
只能调整树中结点指针的指向。

A:左右子树分治，中序遍历，递归实现。根据二叉搜索树的特点，根节点的
左边连接左子树最右边节点，根节点的右边连接右子树的最左边的结点

'''

def Solution:
	def Convert(self, pRootOfTree):
		if not pRootOfTree:
			return None
		if not pRootOfTree.left and not pRootOfTree.right:
			return pRootOfTree

		self.Convert(pRootOfTree.left)
		# 将左子树中中序遍历的最后一个结点指向根
		# 根的左结点指向它
		left = pRootOfTree.left
		if left:
			while left.right:
				left = left.right

			pRootOfTree.left = left
			left.right = pRootOfTree
		self.Convert(pRootOfTree.right)
		right = pRootOfTree.right
		if right:
			while right.left:
				right = right.left
			pRootOfTree.right = right
			right.left = pRootOfTree
		# 遍历到第一个结点
		while pRootOfTree.left:
			pRootOfTree =pRootOfTree.left
		return pRootOfTree
		


