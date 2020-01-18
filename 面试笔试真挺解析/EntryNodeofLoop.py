# -*- encoding:utf-8 -*-
'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null

A: 首先设置两个快慢指针，移动两个指针，若相遇，则存在环
从相遇的地方设置一个指针向后遍历和从头开始遍历相遇为入环点

'''
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def isLoop(self, head):
		if not head or not head.next:
			return None
		slow = head.next
		fast = head.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return slow
		return None

	def EntryNodeOfLoop(self, phead):
		meetNode = self.isLoop(phead)
		if not meetNode:
			return None
		first = phead.next
		second = meetNode
		while first != second:
			first = first.next
			second = second.next
		return first