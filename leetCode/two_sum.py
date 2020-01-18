# -*- encoding:utf-8 -*-

class ListNode:
	def __init__(self, x):
		self.next = None
		self.val = x

class Solution:
	def twoSum(self, nums, target):
		if not nums:
			return -1
		if len(nums) <= 1:
			return -1
		nums_map = {}
		for index, value in enumerate(nums):
			nums_map[value] = index
		for index, value in enumerate(nums):
			if target - value in nums_map:
				index2 = nums_map[target - value]
				if index2 != index:
					return [index + 1, index2 + 1]


	def twoSome1(self, nums, target):
		if not nums or len(nums) <= 1:
			return None
		nums_map = {}
		for index, num in enumerate(nums):
			if target - num in nums_map:
				return [nums_map[target-num], index]
			else:
				nums_map[num] = index
		return None


	def addTwoNumbers(self, pNode1, pNode2):
		if not pNode2 and not pNode1:
			return None
		elif not (pNode1 and pNode1):
			return pNode1 or pNode2
		else:
			if pNode1.val + pNode2.val > 10:
				head = ListNode(pNode2.val + pNode1.val - 10)
				head.next = self.addTwoNumbers(pNode1.next, self.addTwoNumbers(ListNode(1), pNode2.next))
			else:
				head = ListNode(pNode2.val + pNode1.val)
				head.next = self.addTwoNumbers(pNode1.next, pNode2.next)

	# 求最长不重复字串
	def lengthofLengestSubString(self, s):
		if not s:
			return 0
		if len(s) <= 1:
			return len(s)
		locations = [-1 for i in range(256)]
		index = -1
		m = 0
		for i, v in enumerate(s):
			if locations[ord(v)] > index:
				index = locations[ord(v)]
			m = max(m, i - index)
			locations[ord(v)] = i
		return m

	def isPalindrome(self, x):
		if x < 0:
			return False
		elif x != int(str(x)[::-1]):
			return False
		return True


print(Solution().twoSome1([1, 2, 4, 5], 9))