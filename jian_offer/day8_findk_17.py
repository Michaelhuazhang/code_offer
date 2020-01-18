'''
Q:输入一个链表，输出该链表的倒数第K个结点

A: 设置两个指针指向头结点，第一个指针向前走K-1步,走到第k个结点时，第二个指针
和第一个指针同时移动，当第一个指针走到尾结点的时候，第二个指针指向倒数第k个结点
注意链表为空，k=0，k为大于链表的长度的情况


'''

class Solution:
	def FindKthToTail(self, head, k):
		if head == None or k <= 0:
			return None
		pAhead = head
		pBhead = head
		for i in range(k-1):
			if pAhead.next != None:
				pAhead = pAhead.next
			else:
				return None
		while pAhead.next:
			pAhead = pAhead.next
			pBhead = pBhead.next
		return pBhead
		