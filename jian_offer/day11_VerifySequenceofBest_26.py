'''
Q: 判断该数组是不是某二叉排序树的后序遍历的结果
A:根据后序遍历的特点，尾元素一定是根节点
  根据二叉排序树的特点，根的左子树小于根节点，根的柚子树大于根节点

  则序列的前半部分小于尾元素，后半部分大于尾元素
'''

class Solution:
	def VerifySequenceOfBST(self, sequence):
		if sequence == []:
			return False
		length = len(sequence):
		root = sequence[-1]

		for i in range(length):
			if sequence[i] > root:
				break

		for j in range(i, length):
			if sequence[j] < root:
				return False

		left = True
		if i > 0:
			left = self.VerifySequenceOfBST(sequence[:i])
		right = True
		if j < (length - 1):
			right = self.VerifySequenceOfBST(sequence[i:length -1])
		return left and right
		

