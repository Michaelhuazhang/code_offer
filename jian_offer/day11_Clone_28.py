'''
 复制一个复杂链表，这个链表有next和random指针
 A: 复制原始链表中每个节点，将复制的结点连接在原始结点的后面，然后复制后的链表中的复制节电的random指针
 指向被复制节电的random指针的下一个结点，最后拆分
'''
class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution:
	def Clone(self, pHead):
		if not pHead:
			return None
		pNode = pHead
		# 复制节点
		while pNode:
			pClone = RandomListNode(pNode.label)
			pClone.next = pNode.next
			pNode.next = pClone
			pNode = pClone.next

		# 复制random
		pNode = pHead
		while pNode:
			# 找到复制的那个节点
			pClone = pNode.next
			if pNode.random != None:
				pClone.random = pNode.random.next
			pNode = pNode.next
		# 分开链表
		pNode = pHead
		pCloneHead = pCloneNode = pNode.next
		pNode.next = pCloneNode.next
		pNode = pNode.next
		while pNode:
			# 
			pCloneNode.next = pNode.next
			pCloneNode = pCloneNode.next

			pNode.next = pCloneNode.next
			pNode = pNode.next
		return pCloneHead
