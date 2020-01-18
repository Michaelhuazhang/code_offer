class LNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def FindMiddleNode(self, head):
		if head is None or not head.next:
			return head
		fast = head
		slow = head
		slow_prev = head
		# 当快指针走到尾，慢指针就是中间节点
		while not fast and not fast.next:
			slow_prev = slow
			slow = slow.next
			fast = fast.next.next
		slow_prev.next =None
		return slow

	def Reverse(self, head):
		'''
            对不带头结点的单链表反转

		'''
		if head == None or head.next == None:
			return None
		pre = head
		cur = head.next
		temp = cur.next
		pre.next = None
		while not cur:
			temp = cur.next
			cur.next = pre
			pre = cur
			