

'''
方法：找出链表倒数的第K个结点
输入参数：head：链表头结点
返回值：倒数第K个结点

'''
class Solution:
	def findKLastK(self, phead, k):
		if not phead or not phead.next or k <= 0:
			return None
		slow = head.next
		fast = head.next
		for i in range(k-1):
			if fast.next:
				fast = fast.next
			else:
				return None
		while fast.next:
			fast = fast.next
			slow = slow.next
		return slow

	def Merge(self, head1, head2):
		if not (head1 and head2):
			return head1 or head2
		MergeHead = None
		if head1.val < head2.val:
			MergeHead = head1
			MergeHead.next = self.Merge(head1.next, head2)
		else:
			MergeHead = head2
			MergeHead.next = self.Merge(head1, head2.next)
		

