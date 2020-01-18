


class Solution:
	'''
     判断一个带头结点的链表是否有环，并输出
	'''
	def isLoop(self, phead):
		if not phead or not phead.next:
			return None
		slow = phead.next
		fast = phead.next
		while not fast.next and not fast:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return slow
		return None

	'''
    找出环的入口点
	'''
	def findLoopNode(self, phead, meetNode):
		first = phead.next
		second = meetNode
		while fist != second:
			fist = fist.next
			second = second.next
		return first


