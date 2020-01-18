# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 16:53
# @Author  : Michael Zhang
# @Site    : 
# @File    : merge_listNode.py
# @Software: Sublime

'''
Q: 输入连个单调递增的链表，输出两个链表合并后的链表，保持单调不减

A:每个链表设置一个指针，合并时，比较头结点的大下，小的作为合并后链表的头结点，再比较
剩余部分和另一个部分链表的头结点，取小的，一直循环此过程
'''
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def Merge(self, pHead1, pHead2):
		if pHead2 == None:
			return pHead1
		if pHead1 == None:
			return pHead2
		pMergeHead = None

		if pHead1.val < pHead2.val:
			pMergeHead = pHead1
			pMergeHead.next = self.Merge(pHead1.next, pHead2)
		else:
			pMergeHead = pHead2
			pMergeHead.next = self.=Merge(pHead1, pHead2.next)
		return pMergeHead
	