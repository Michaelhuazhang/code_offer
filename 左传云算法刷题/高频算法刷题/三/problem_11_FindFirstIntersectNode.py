# -*- encoding:utf-8 -*-

# Q: 查找两个单链表是否相交
# 判断单链表是否有环，若有环，找到环的入点
# 一个有环一个无环，不可能相交
# 两个都无环，判断长度，遍历第一个相等的结点
# 二个都有环：存在环的入点是相同的/环的结点是不同的，但是共享一个环/两个环是独立的一定不相交


class Node:
	def __init__(self, data):
		self.val = data
		self.next = None

class Solution:
	def getInsertNode(self, head1, head2):
		if not head1 or not head2:
			return None

		loop1 = self.getLoopNode(head1)
		loop2 = self.getLoopNode(head2)
		if not loop2 and not loop1:
			return self.noloop(head1, head2, None)
		if loop1 and loop2:
			return self.bothloop(head1,loop1, head2, loop2)
		return None

	def getLoopNode(self, head):
		if not head or not head.next or not head.next.next:
			return None
		#head 为头结点
		fast = head.next.next
		slow = head.next
		while fast != slow:
			if not fast.next and not fast.next.next:
				return None
			fast = fast.next.next
			slow = slow.next
		fast = head # 相遇后，快指针到开头，一起遍历
		while fast != slow:
			fast = fast.next
			slow = slow.next
		return fast

	def noloop(self, head1, head2, end):
		if not head1 or not head2:
			return None
		# 先求出各自长度，短的先走少的长度，然后一起遍历，遇到相等的为相交的
		cur1 = head1
		cur2 = head2
		length = 0
		while cur1.next != end:
			length += 1
			cur1 = cur1.next
		while cur2.next != end:
			length -= 1
			cur2 = cur2.next
		if cur2 != cur1:
			return None
		cur1 = head1 if n > 0 else head2
		cur2 = head2 if cur1 == head1 else head1
		n = abs(n)
		while n > 0:
			cur1 = cur1.next
			n -= 1
		while cur1 != cur2:
			cur2 = cur2.next
			cur1 = cur1.next
		return cur1

	def boothloop(self, head1, loop1, head2, loop2):
		# 三种情况
		cur1 = None
		cur2 = None
		if loo1 == loop2:
			return self.noloop(head1, head2, loop1)
		else:
			# 从一个环遍历是否能够遍历到另一个环
			cur1 = loop1.next
			while cur1 != loop1:
				if cur1 == loop2:
					return loop2
				cur1 = cur1.next
		return None

