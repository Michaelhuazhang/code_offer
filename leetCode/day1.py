# -*- encoding:utf-8 -*-

# Q: Two Sum

class Node():
	def __init__(self, val):
		self.next = None
		self.val = val


class Solution:
	def twoSum(self, array, nums):
		dicts = {}
		if not array or len(array) == 0:
			return 0
		for index, value in enumerate(array):
			if nums - value in dicts:
				return [dicts[nums - value], index]
			else:
				dicts[value] = index
		return False

	def addTwoNumbers(self, head1, head2):
		if not head1 and  not head2:
			return
		elif (head1 or head2):
			return head1 or head2
		else:
			if head1.val + head2.val < 10:
				head = Node(head1.val + head2.val)
				head.next = self.addTwoNumbers(head1.next, head2.next)
			else:
				head = Node(head1.val + head2.val - 10)

				head.next = self.addTwoNumbers(self.addTwoNumbers(head1.next, Node(1)), head2.next)
		return head

	def lengthOfLongestSubString(self, s):
		# 记录每个字符结尾的最长字串
		# 碰到一个已经出现的字符，从该字符出现的index+1开始计算
		# 一个字典，将出现的字符作为键，值作为下标，如果不在字典中
		# 将其加入，如果在字典中，比较该字符的值是否大于起点
		res, start, n = 0, 0, len(s)
		maps = {}
		for i in range(n):
			start = max(start, maps.get(s[i], -1) + 1)
			res = max(res, i - start + 1)
			maps[s[i]] = i
		return res



array = [1, 2, 4, 5, 6]


print(Solution().twoSum(array, 6))
print(Solution().lengthOfLongestSubString("abbbbbbacd"))