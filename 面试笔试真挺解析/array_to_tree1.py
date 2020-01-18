# encoding:utf-8 -*- 
# 
'''
Q: 将一个有序数组转换成二叉树
'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def arraytotree(self, arr, start, end):
		if end >= start:
			mid = (end + start + 1) / 2
			root = TreeNode(arr[mid])
			root.left = self.arraytotree(arr, start, mid - 1)
			root.right = self.arraytotree(arr, mid + 1, end)
		else:
			root = None
		return root

	def printTreeMidOrder(self, root):
		if not root:
			return
		if root.left:
			self.printTreeMidOrder(root.left)
		print(" " + str(root.val))
		if root.right:
			self.printTreeMidOrder(root.right)

if __name__ == "__main__":
	array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print("Array:", array)
	root = Solution().arraytotree(array, 0, len(array) -1)
	print("-------------")
	Solution().printTreeMidOrder(root)


