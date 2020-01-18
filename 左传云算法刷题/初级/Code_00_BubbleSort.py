# -*- encoding:utf-8 -*-

# 冒泡排序
# 每次排好一个位置，左右不断交换
# 将最大的放在最后

class Solution:
	def bubblesort(self, array):
		if not array or len(array) < 2:
			return array
		for i in range(len(array)-1, -1, -1):
			for j in range(i):
				if array[j] > array[j + 1]:
					array[j], array[j+1] = array[j+1], array[j]
		return array


print(Solution().bubblesort([5, 4, 2, 7, 4, 6, 1]))