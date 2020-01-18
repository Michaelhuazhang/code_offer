# -*- encoding:utf-8 -*-

class Solution:
	def maxlengthAweSome(self, array, k):
		if not array or len(array) == 0:
			return 0
		sums = [0 for i in range(len(array))]
		ends = {}
		sums[len(array) - 1] = array[len(array) - 1]
		ends[len(array) - 1] = len(array) - 1
		for i in range(len(array)-2, -1, -1):
			if sums[i+1] < 0:
				sums[i] = array[i] + sums[i+1]
				ends[i] = ends[i+1]
			else:
				sums[i] = array[i]
				ends[i] = i
		end = 0
		sumarray = 0
		res = 0
		for i  in range(len(array)):
			while end < len(array) and sumarray + sums[end] <= k:
				sumarray += sums[end]
				end = ends[end] + 1
			sumarray -= array[i] if end > i else 0
			res = max(res, end - i)
			end = max(end, i+1)
		return res
print(Solution().maxlengthAweSome([1, 7, 9, -5, -4, 3, 2, 4, -4, 2], 7))
