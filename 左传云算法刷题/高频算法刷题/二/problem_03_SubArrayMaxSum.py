# -*- encoding:utf-8 -*-

#  Q: 给定一个数组，返回子数组的最大累加和
# A: 最大累加和肯定不能为负，如负，我们不需要它
import sys
class Solution:
	def maxSum(self, array):
		if not array or len(array) == 0:
			return 0
		maxs = -sys.maxsize
		cur_sums = 0
		for i in array:
			cur_sums += i
			maxs = max(maxs, cur_sums)
			cur_sums = 0 if cur_sums < 0 else cur_sums
		return maxs

print(Solution().maxSum([ -2, -3, -5, 40, -10, -10, 100, 1])) 