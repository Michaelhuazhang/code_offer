# -*- encoding:utf-8 -*-

class Solution:
	def subArraymaxSum(self, array):
		if not array or len(array) < 2:
			return 0
		rightsubsum = [0 for i in range(len(array))]
		maxs = -10000000
		cur = 0
		for i in range(len(array) -1, 0, -1):
			cur += array[i]
			maxs = max(cur, maxs)
			rightsubsum[i] = maxs
			cur = 0 if cur < 0 else cur
		res = array[0]
		cur = 0
		maxs = -1000000
		for i in range(len(array)-1):
			cur += array[i]
			maxs = max(maxs, cur)
			res += max(res, maxs + rightsubsum[i+1])
			cur = 0 if cur < 0 else cur
		return res

print(Solution().subArraymaxSum([4, 5, 3, 1, 7, 5]))