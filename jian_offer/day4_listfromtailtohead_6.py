# -*- coding: utf-8 -*-
# @Time    : 2019/01/14 20:39
# @Author  : Michael Zhang
# @Site    : 
# @File    : day4_listfromtailtohead_6.py
# @Software: Sublime

'''
Q: 输入一个链表，按链表值从尾到头按顺序返回一个ArrayList

A: 是否可以对链表结构进行修改
   若是：修改，遍历
   否则：将链表的值遍历放入栈中，然后输出/或者直接每次插入输出链表中的第一个位置
   先进后出
'''
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def  printListFromTailToHead(self, listNode):
		if not listNode:
			return []
		result = []
		while (listNode):
			result.insert(0, listNode.val)
			listNode = listNode.next
		return result
