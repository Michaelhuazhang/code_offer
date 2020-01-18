# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 16:11
# @Author  : Michael Zhang
# @Site    : 
# @File    : FindKthTotail.py
# @Software: Sublime

'''
Q: 输入一个链表，输出该链表中倒数第K个结点

A: 设置两个指针指向头结点，第一个指针，第一个指针向前走k-1步，走到第k个测点，此时第二个测点和第一个指针同时移动，
当第一个指针到尾结点的时候，第二个指针指向倒数第K个结点，注意链表为空，k=0，k大于链表的长度的情况
'''
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def FindKthToTail(self, head, k):
		if head == None or k <= 0:
			return None
		pAhead = head
		pBhead = None

		for i in range(k-1):
			if pAhead.next != None:
				pAhead = pAhead.next
			else:
				return None
		pBhead = head

		while pAhead.next != None:
			pAhead = pAhead.next
			pBhead = pBhead.next
		return pBhead
		