'''
两个单链表相加


'''
class Node:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def add(self, pHead1, pHead2):
		if pHead2 is None or pHead2.next is None:
			return pHead1
		if pHead1 is None or pHead1.next is None:
			return pHead2

		c = 0 # 代表进位
		sums = 0
		pNode1 = pHead1.next
		pNode2 = pHead2.next
		pAddHead = Node()
		rear = pAddHead
		while pNode2 is not None and pNode1 is not None:
			temp = Node()
			sums = pNode1.val + pNode2.val + c

			temp.val = sums % 10
			c = sums / 10
			rear.next = temp
			rear = temp# 尾插，保持顺序
			pNode2 = pNode2.next
			pNode1 = pNode1.next
		while pNode1:
			temp = Node()
			sums = pNode1.val + c
			temp.val = sums % 10
			c =sums / 10
			rear.next = pNode1
			rear = pNode1
			pNode1 = pNode1.next
		while pNode2:
			temp = Node()
			sums = pNode2.val + c
			temp.val = sums % 10
			c =sums / 10
			rear.next = pNode2
			rear = pNode2
			pNode2 = pNode2.next
		if c == 1:
			temp = Node(1)
			rear.next = temp
			rear = temp
		return pAddHead

	def addTwoNumbers(self, pHead1, pHead2):
		if not pHead1 and not pHead2:
			return
		elif not (pHead1 and pNode2):
			return pHead2 or pHead1
		else:
			if pHead1.val + pHead2.val < 10:
				pAddHead = Node(pHead2.val + pHead1.val)
				pAddHead.next = self.addTwoNumbers(pHead1.next,pHead2.next)
			else:
				pAddHead = Node(pHead2.val + pHead1.val -10)
				pAddHead.next = self.addTwoNumbers(pHead1.next, self.addTwoNumbers(pHead2.next, Node(1)))

		return pAddHead
