
import collections


class Solution:
	def removeDup(self, pHead):
		if pHead.next == None: 
			return None
		if pHead.next.next == None:
			return pHead
		Nodedict = collections.OrderDict()
		pNode = pHead.next
		prev = pHead
		while pNode:
			temp = pNode.next
			if pNode.val not in Nodedict:
				Nodedict[pNode.val] = 1
				prev = pNode
			else:
				Nodedict[pNode.val] += 1
				prev.next = pNode.next
			pNode = temp
		return 



