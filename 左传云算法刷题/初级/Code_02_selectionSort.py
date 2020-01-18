# -*- encoding:utf-8 -*-

# 选择类排序

# 每次选择一个最小的元素放在一个位置上，不提前交换

class Solution:
	def selectSort(self, array):
		if not array or len(array) < 2:
			return array
		for i in range(len(array)-1):
			minindex = i
			for j in range(i+1, len(array)):
				# 选择最小的
				if array[j] < array[minindex]:
					minindex = j
			array[i], array[minindex] = array[minindex], array[i]
		return array
print(Solution().selectSort([5, 2, 7, 9, 1]))