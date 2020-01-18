# -*- encoding:utf-8 -*-
'''
Q : 求出数组中唯一的重复元素

A: hashSet
B: 所有数相加-定值等于那个数
C:异或位运算，任何数和0异或为任何数，
'''
print(2^2^2)

class Solution:
	def findDup(self, array):
		if array == None:
			return -1
		lens = len(array)
		result = 0
		for i in array:
			result ^= i
		for j in range(1, len(array)):
			result ^= j
		return result

print(Solution().findDup([1, 3, 4, 2, 5, 3]))

class MaxMin:
	def getMaxMin(self, array, start, end):
		if array == None:
			return
		min_max = []
		mid = (start + end) / 2
		if start == end:
			min_max.append(array[start])
			min_max.append(array[end])
			return min_max
		if end - start == 1:
			if array[start] >= array[end]:
				min_max.append(array[end])
				min_max.append(array[start])
			else:
				min_max.append(array[start])
				min_max.append(array[end])
			return min_max	
		Lmin_max = self.getMaxMin(array, start, mid)
		Rmin_max = self.getMaxMin(array, mid + 1, end)

		min_max.append(min(Lmin_max[0], Rmin_max[0]))
		min_max.append(max(Lmin_max[1], Rmin_max[1]))

		return min_max

print(2 ^ 8)