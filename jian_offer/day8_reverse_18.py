'''
输入一个链表，反转链表后，输出链表的表头

'''

class Solution:
	def ReverseList(self, pHead):
		pReversedHead = None
		pNode = pHead
		nPrev = None

		while pNode != None:
			pNext = pNode.next
			if pNext == None:
				pReversedHead = pNode
			pNode.next = nPrev
			nPrev = pNode
			pNode = pNext
		return pReversedHead
		