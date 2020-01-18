# -*- encoding:utf-8 -*-

class Solution:
	def manacherString(self, strs):
		strs_list = list(strs)
		res = [1] * (len(strs) * 2 + 1)
		for i in range(0, len(res)):
			res[i] = "#" if (i & 1) == 0 else strs_list[i]
		return res

	def maxLcpsLength(self, strs):
		if not strs or len(strs) == 0:
			return 0
		strs_list = self.manacherString(strs)
		pArray = [0] * len(strs_list) # 回文半径数组
		c = -1
		r = -1
		maxn = -10
		for i in range(len(strs_list)):
			pArray[i] = min(pArray[2 * c - i], r - i) if r > i else 1
			while (i + pArray[i] < len(strs_list) and i - pArray[i] > -1):
				if pArray[i + pArray[i]] == pArray[i - pArray[i]]:
					pArray[i] += 1
				else:
					break

			if (i + pArray[i] > r):
				r = i + pArray[i]
				c = i
			maxn = max(maxn, pArray[i])
		return maxn - 1
		

