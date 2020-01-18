# encoding:utf-8 -*- 
# 
'''
Q: 将一个有序数组转换成二叉树,层次遍历

'''
from collections import deque
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
	'''
     层次遍历，利用队列
	'''
	def printTreeLayer(self, root):
		if not root:
			return
		queue = []
		queue.append(root)
		while queue:
			temp = queue.pop(0)
			print(" " + str(temp.val))
			if temp.left:
				queue.append(temp.left)
			if temp.right:
				queue.append(temp.right)
	def printTreeLevel(self, root):
		if not root:
			return
		queue = deque()
		queue.append(root)
		while queue:
			temp = queue.popleft()
			print(" " + str(temp.val))
			if temp.left:
				queue.append(temp.left)
			if temp.right:
				queue.append(temp.right)

	def printAtLevel(self, root, level):
		if not root or level < 0:
			return 0
		elif level == 0:
			return root.data
		else:
			return self.printAtLevel(root.left, k-1) + self.printAtLevel(root.right, k-1)
if __name__ == "__main__":
	array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print("Array:", array)
	root = Solution().arraytotree(array, 0, len(array) -1)
	print("-------------")
	# Solution().printTreeLayer(root)
	Solution().printTreeLevel(root)
