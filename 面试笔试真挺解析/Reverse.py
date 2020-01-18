

# 实现带头结点的链表的反转
# 
class Solution:
	def Reverse_Head(self, head):
		if head == None or head.next == None:
			return 
		cur = head.next.next
		head.next.next = None
		while cur:
			temp = cur.next
			cur.next = head.next
			head.next = cur
			cur = temp
		return head

	def Reverse(self, Node):
		if Node == None:
			return 
		if Node.next == None:
			returm Node
		head = Node
		head.next = None
		Node = Node.next
		while Node:
			temp = Node.next
			Node.next = head
			head = Node
			Node = temp
		return head
		
