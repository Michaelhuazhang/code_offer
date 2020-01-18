# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 16:33
# @Author  : Michael Zhang
# @Site    : 
# @File    : ReverseListNode.py
# @Software: Sublime

'''
Q: 输入一个链表，反转链表后，输出链表的开头
A:主要注意当头结点为空，或者一个链表只有一个结点是，翻转后的链表断裂，返回的翻转之后的头结点不是原来的尾结点
所以需要一个翻转后的头结点，一个指向当前节点的指针，两个分别指向当前节点的前后节点的指针
防止断裂，也可以使用递归


'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def reverseList(self, pHead):
		# 新链表的头结点
		preverseHead = None
		pNode = pHead
		pPrev = None
		while pNode != None:
			pNext = pNode.next
			if pNext == None:
				preverseHead = pNode # 若链表已经遍历结束
			pNode.next = pPrev
			pPrev = pNode
			pNode = pNext
		return preverseHead
	

