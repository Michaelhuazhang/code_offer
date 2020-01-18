# -*- encoding:utf-8 -*-

# 找出交错字串,求出最长的字串
# 依次遍历，记录每个开头的最长不同字串
# 更新长度


# 找出一个最长的连续字串，这个字串是0和1的数量相等

# 将0变为-1，最长和为0的连续子串
# 准备一个map存放   和：下标

# 不断累加和放入map当中，查找sum-aim最早出现，就是最长的



class Solution:
	def jiaocuo(self, s):
		if not s or len(s) == 0:
			return 0
		maxs = 1
		count = 1
		for i in range(1, len(s)):
			count += 1
			if s[i] == s[i-1] :
				count = 1
			maxs = max(maxs, count)
		return maxs

	def maxlength(self, array, k):
		if not array or len(array) == 0:
			return 0
		dicts = {0:-1}
		lens = 0
		sums = 0
		for i in range(len(array)):
			sums += array[i]
			if (sums - k) in dicts:
				lens = max(lens, i - dicts[sums-k])
			if sums not in dicts:
				dicts[sums] = i
		return lens

 