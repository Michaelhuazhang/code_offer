'''
输入一颗二叉树的根节点和一个整数，打印出二叉树中节点值的和为输入整数的所有
路径。路径的定义为从树的根节点开始往下一直到叶节点所经过的结点形成一条路径

A : 路径是根节点出发到叶子节点
    以根节点为起始节点，我们首先需要遍历根节点。故选取前序遍历

    前序遍历的方式访问二叉树的结点，当访问到一个结点是，将结点加入到路径中
    并累计节点的值，直到访问到符合要求的结点或者叶节点。然后递归访问该节点的父节点
    在函数退出时减去当前节点的值。实际上是一个入栈和出栈的过程

'''

class Solution:
	def FindPath(self, root, expectNumber):
		if not root or root.val > expectNumber:
			return []
		if not root.left and not root.right and root.val == expectNumber:
			return [[root.val]]

		else:
			expectNumber -= root.val
			left = self.FindPath(root.left, expectNumber)
			right = self.FindPath(root.right, expectNumber)

			result = [[root.val]+i for i in left]
			for i in right:
				result.append([root.val]+i)

		return sorted(result, key=lambda x: -len(result))
