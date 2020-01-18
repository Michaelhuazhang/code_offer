# -*- encoding:utf-8 -*-
# Q:给出一堆数组，这个数组中最多存在一对不同颜色的相邻砖块
# 计算有几种方式将砖块排成一行
# A 如果数组中存在三种以上不同的颜色，则无法
# 二种不同的颜色，则两种
# 一种颜色，则就一种

class Solution:
	def counts(self, array):
		times = 0
		if not array or len(array) == 0:
			return 0
		sets = set()
		for i in array:
			if i not in sets:
				sets.add(i)
				times += 1
		if times > 2:
			return 0
		elif times == 2:
			return 2
		else:
			return counts


