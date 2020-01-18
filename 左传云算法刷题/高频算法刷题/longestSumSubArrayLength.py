# -*- encoding:utf-8 -*-

'''
 数组中有正有负，累计额和等于k最长的子数组长度
'''

class Solution:
	def maxlength(self, array, k):
		if not array or len(array) == 0:
			return 0
		arraydict = {0:-1}
		lens = 0
		sums = 0
		for i in range(len(array)):
			sums += array[i]
			if (sums - k) in arraydict.keys():
				lens = max(lens, i - arraydict[sums-k])
			if sums not in arraydict.keys():
				arraydict[sums] = i
		return lens

print(Solution().maxlength([4, 0,9, 4,2, -4, -2, 5, 4, 3, 2, -2, 2], 9) )