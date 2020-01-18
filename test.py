#!/usr/bin/env python  
# coding=utf-8  
'''
输入两个整数序列，第一个为栈的压入顺序，判断第二个序列是否为栈的弹出序列

A:建立一个辅助栈，把push的数字依次压入入栈，每次压入后，比较辅助栈的栈顶
和POP的序列的首元素是否相等，相等的话，就推
'''

class Solution:
	def IsPopOrder(self, pushV, popV):
		if pushV == [] or popV == []:
			return False
		stack = []
		for i in pushV:
			stack.append(i)
			while len(stack) and stack[-1] == popV[0]:
				stack.pop()
				popV.pop(0)
		if len(stack):
			return False
		else:
			return True



'''
Q:从下往上打印出二叉树的每个节点，同层次从左到右打印

A: 引入一个队列，每次打印一个节点的时候，如果该节点有子节点，则把
该节点的子节点放在一个队列的末尾，取出队列头部的最早进入队列的结点

'''

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def PrintFromTopToBottom:
		# 返回从上到下的从左到右的每个节点值列表
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

'''
Q:  输入一个数组，判断该数组是不是某二叉排序树的后序遍历的结果

A: 根据后序遍历的特点，尾元素一定是根节点，同时小于尾元素的值是左子树，大于尾元素的值是右子树
且序列前半部分小于尾元素，后半部分大于尾元素，可以将序列划分为左子树序列和柚子树序列，然后递归
'''

class Solution:
	def VerifySequenceOfBST(self, sequence):
		if sequence == []:
			return False
		length = len(sequence)
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
		if j < length -1:
			right = self.VerifySequenceOfBST(sequence[i:length-1])
		return left and right




'''
Q: 二叉树中和为某一值的路径

A： 用前序遍历的方式访问二叉树的结点，当访问到一个结点时，将该节点加到路径当中，并累计节点的值，直到
访问到符合要求的结点或者访问到叶节点，然后递归访问该节点的父节点，在函数退出时要删除该节点，并减去当前节点的值
实际上是一个出栈和入栈的过程

'''

class Solution:
	def findPath(self, root,expectNumber):
		if not root or root.val > expectNumber:
			return []
		if not root.left and not root.right and root.val == expectNumber:
			return [[root.val]]
		else:
			expectNumber -= root.val
			left = self.findPath(root.left, expectNumber)
			right = self.findPath(root.right, expectNumber)

			result = [[root.val] + i for i in left]

			for i in right:
				result.append([root.val] + i)
		return sorted(result, key=lambda x:-len(x))


'''
Q: 复杂链表（节点值，一个指向下一个结点，另一个特殊指针指向任意一个结点）

A ： 复制原始链表的每一个结点，将复制的结点连接在其原始结点的后面，然后将复制后的链表中的random指针

指向复制节点的random指针指向节点的下一个结点，最后拆分链表，拆分成原始链表的新链表和复制节点的复制链表

'''
class RandomListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		self.random = None

class Solution:
	def Clone(self, pHead):
		if not pHead:
			return None
		pNode = pHead

		while pNode:
			pClone = RandomListNode(pNode.val)
			pClone.next = pNode.next
			pNode.next = pClone
			pNode = pClone.next
		pNode = pHead




'''
Q: 字符串的排列  如果输入一个字符串，按字典序打印出该字符串中所有排列‘


A: 先固定第一个元素，求出后缪按的排列；重新固定第一个元素
依次

'''

class Solution:
	def Permutation(self, ss):
		if not ss:
			return []
		if len(ss) == 1:
			return list(ss)

		charList = list(ss)
		charList.sort()
		pStr = []
		for i in range(0, len(charList)):
			if i > 0 and charList[i] == charList[i-1]:
				continue # 防止同一个字母开头
			temp = self.Permutation("".join(charList[:i]) + "".join(charList[i+1:]))
			for j in temp:
				pStr.append(charList[i] + j)
		return pStr
		
