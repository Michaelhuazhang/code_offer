# -*- encoding:utf-8 -*-
# 一个数组中，相邻差值最大和
# 排序

# 最小和最大放一起
# 次小和最大，次大和最小放在一起
# 奇数，判断哪边大放哪边
# 偶数，正好不用处理


class Solution:
	def maxMad(self, array):
		if not array or len(array) < 2:
			return 0
		array.sort()
		res = array[-1] - array[0]
		maxI = len(array) - 2
		minI = 1
		while minI < maxI:
			res += array[maxI + 1] - array[minI] # 最大-次小
			res += array[maxI] - array[minI-1]    # 次大-最小
			minI += 1
			maxI -= 1
		if minI == maxI:
			# 奇数，放在两侧，哪侧最大，选哪侧
			res += max(array[maxI + 1] - array[minI], array[maxI] - array[minI - 1])
		return res

array = [ 1, 8, 2]
print(Solution().maxMad(array))