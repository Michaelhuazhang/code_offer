'''
查找第一个公共结点

A:依次遍历每一个链表，当链表的长度为m和n，假设m>n,就先让长的链表走m-n个结点，同时遍历，遇到相同的结点就停止可以



'''
class Solution:
	def FindFirstCommonNode(self, phead1, phead2):
		if not phead2 or not phead1:
			return None
		p1, p2 = phead1, phead2
		len1, len2 = 0
		while p1.next:
			p1 = p1.next
			len1 += 1
		while p2.next:
			p2 = p2.next
			len2 += 1
		if p1 == p2:
			if len1 > len2:
				while len1 - len2:
					phead1 = phead1.next
					len1 -= 1
			else:
				while len2 - len1:
					phead2 = phead2.next
					len2 -= 1
			while phead1 and phead2:
				if phead1 == phead2:
					return phead1
				phead1 = phead1.next
				phead2 = phead2.next
		return None

