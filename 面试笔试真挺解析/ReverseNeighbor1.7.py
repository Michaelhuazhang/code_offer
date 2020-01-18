
class LNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:

	def reverse(self, phead):
		'''
         实现相邻数据的逆置
		'''
		if not phead or not phead.next:
			return None
		cur = phead.next
		pre = head
		while cur:
			temp = cur.next.next
			pre.next = cur.next
			cur.next.next = cur
			cur.next = temp
			pre = cur
			cur = temp



