# -*- encoding:utf-8 -*-
# @Author:ZJH
# @Time: 2019/3/8    21:12

# 荷兰国企问题


# 将一堆数组中小于num放左边，大于num放右边

# 进阶：将一对数组中，小于num放左边，num放中间，大于num放右边


# 问题1：两个指针，cur指针，less指针，依次遍历每一个数组
# 若小于num，less指针+1，将cur和less+1数组交换，cur+1
# 若大于num，cur+1


# less,more,cur 指针

# 注意more交换，cur不动，less交换，cur+1



# 改进快排，是将每一次划分后，中间等于的区域不用再次进行排序


class Solution:
	def partition(self, array, num):
		if not array or len(array) <= 1:
			return array
		less = -1

		for cur in range(len(array)):
			if array[cur] < num:
				less += 1
				# less 和cur 交换
				array[less], array[cur] = array[cur], array[less]
		return array

	def partitionequalnum(self, array, left, right, num):
		if not array or len(array) <= 1:
			return array
		less = left - 1
		more = right + 1
		while left < more:
			if array[left] < num:
				less += 1
				array[less], array[left] = array[left], array[less]
				left += 1
			elif array[left] > num:
				more -= 1
				array[more], array[left] = array[left], array[more]
			else:
				left += 1
		return array, less, more

print(Solution().partition([1,7,2,4,3,4,4,1,2], 4))
print(Solution().partitionequalnum([1,7,2,4,3,4,4,1,2], 0, 8, 4))

class Solution1:
	def heapSort(self, array):
		if not array or len(array) < 2:
			return array
		for i in range(len(array)):
			self.heapInsert(array, i)
		size = len(array)
		array[0], array[size-1] = array[size-1], array[0]
		size -= 1
		while size>0:
			self.heapify(array, 0, size)
			array[0], array[size-1] = array[size-1], array[0]
			size -= 1

	def heapify(self, array, index, size):
		# size,代表堆的大小
		# index ，代表开会调整的位置
		left = index * 2 + 1
		while left < size:
			largest = left + 1 if array[left + 1] > array[left] and left + 1 < size else left
			largest = largest if array[largest] > array[index] else index
			if largest == index:
				break
			array[index], array[largest] = array[largest], array[index]
			index = largest
			left = 2 * index + 1
	 
		

	def heapInsert(self, array, index):
		while array[index] > array[(index - 1) / 2]:
			array[index], array[index-1] = array[index-1], array[index]
			index = (index - 1)/2