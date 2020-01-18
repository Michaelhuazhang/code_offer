# -*- encoding:utf-8 -*-

# 直接插入排序
# 从第二个元素开始插入前面合适的位置上

class Solution:
	def insertSort(self, array):
		if not array or len(array) < 2:
			return array
		for i in range(1, len(array)):
			for j in range(i-1, -1, -1):
				if array[j] > array[j+1]:
					array[j], array[j+1] = array[j+1], array[j]
		return array

print(Solution().insertSort([6, 5, 4, 1, 4]))
