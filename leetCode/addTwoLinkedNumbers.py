# -*- encoding:utf-8 -*-

class Node():
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():
	def addTwoLinkedNumbers(self, head1, head2):
		if not head2 and not head1:
			return None
		elif not head1 or not head2:
			return head2 or head1
		else:
			new = head1.val + head2.val
			temp = Node()
			head = None
			if new > 10:
				temp.val = new%10
				newNode = self.addTwoLinkedNumbers(self.addTwoLinkedNumbers(head1.next, Node(1)), head2.next)
				newNode.next = temp
				head = newNode

			else:
				temp.val = new
				newNode = self.addTwoLinkedNumbers(self.head1.next, self.head2.next)
				newNode.next = temp
				head = newNode
			return head
			


