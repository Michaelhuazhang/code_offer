# -*- encoding:utf-8 -*-

class Solution:
	# 快排
	def bubbleSort(self, array):
		'''
           冒泡排序：每次交换，将最大的放在最后一位

		'''
		if not array or len(array) < 2:
			return array
		for i in range(len(array) -1, 1, -1):
			for j in range(i):
				if array[j] > array[j+1]:
					array[j], array[j+1] = array[j+1], array[j]
		return array
    # 插入排序
	def insert_sort(self, array):
		'''
         从头开始每次插入一个位置
		'''
		if not array or len(array) < 2:
			return array
		for i in range(1, len(array)):
			for j in range(i-1, -1, -1):
				if array[j] > array[j + 1]:
					array[j], array[j + 1] = array[j+1], array[j]
				else:
					break
		return array

	def selection_sort(self, array):
		'''
           选择排序
		'''
		if not array or len(array) < 2:
			return array
		for i in range(len(array) - 1):
			minindex = i
			for j in range(i+1, len(array)):
				minindex = j if array[j] < array[minindex] else minindex
			array[i], array[minindex] = array[minindex], array[i]
		return array

	def heapSort(self, array):
		'''
          堆排序
		'''
		if not array or len(array) < 2 :
			return array
		for i, v in enumerate(array):
			self.heapInsert(array, i)
		array[0], array[len(array) - 1] = array[len(array) -1], array[0]
		size = len(array) -1
		while size:
			self.heapify(array, 0, size)
			size -= 1
			array[0], array[size] = array[size], array[0]
		return array

	def heapInsert(self, array, index):
		while array[index] > array[(index-1) /2] :
			array[index], array[(index-1) /2] = array[(index-1) /2], array[index]
			index = (index-1) /2

	def heapify(self, array, index, size):
		left = index * 2 + 1
		while left < size:
			largest = left + 1 if (left+1) < size and array[left+1] > left else left
			largest = largest if array[largest] > array[index] else index
			if largest == index:
				break
			# 不用调整
			array[largest], array[index] = array[index], array[largest]
			index = largest
			left = index * 2 + 1

	def QuickSort(self, array):
		if not array or len(array) < 2:
			return array
		self.quickSort(array, 0, len(array) - 1)
		return array

	def quickSort(self, array, left, right):
		import random
		if left < right:
			array[right], array[random.randint(left, right)] = array[random.randint(left, right)], array[right]
			l, r = self.partition(array, left, right)
			self.quickSort(array, left, l - 1)
			self.quickSort(array, r + 1, right)

	def partition(self, array, left, right):
		less = left - 1
		more = right
		while left < more:
			if array[left] < array[right]:
				less += 1
				array[less], array[left] = array[left], array[less]
				left += 1
			elif array[left] > array[right]:
				more -= 1
				array[more], array[left] = array[left], array[more]
			else:
				left += 1
		array[more], array[right] = array[right], array[more]
		return less +1, more

	# 归并排序
	def merge_sort(self, array):
		if not array or len(array) < 2:
			return array
		self.mergeSort(array, 0, len(array) - 1)
		return array

	def mergeSort(self, array, left, right):
		if left == right:
			return
		mid = left + ((right-left) >> 1)
		self.mergeSort(array, left, mid)
		self.mergeSort(array, mid+1, right)
		self.merge(array, left, mid, right)

	def merge(self, array, left, mid, right):
		helparray = [0 for i in range(right-left + 1)]
		index, p1, p2 = 0, left, mid+1
		while (p1 <= mid) and (p2 <= right):
			if array[p1] < array[p2]:
				helparray[index] = array[p1]
				p1 += 1
			else:
				helparray[index] = array[p2]
				p2 += 1
			index += 1
		while p1 <= mid:
			helparray[index] = array[p1]
			index += 1
			p1 += 1
		while p2 <= right:
			helparray[index] = array[p2]
			index += 1
			p2 += 1
		for i,v in enumerate(helparray):
			array[left+i] = v













# print(Solution().bubbleSort([4]))
# print(Solution().insert_sort([2, 4, 6, 1, 3, 8, 9, 7]))
# print(Solution().selection_sort([4, 1, 2, 7, 6, 8, 3]))
# print(Solution().heapSort([2, 4, 6, 1, 3, 8, 9, 7]))
# print(Solution().QuickSort([2, 4, 6, 1, 3, 8, 9, 7]))

# import random
# print(random.randint(1, 100))
print(Solution().merge_sort([2, 4, 6, 1, 3, 8, 9, 7]))