# -*- encoding:utf-8 -*-

class Solution:
	def quickSort(self, array):
		if not array:
			return []
		if len(array) == 1:
			return array
		pivot = array[0]
		left = self.quickSort([i for i in array[1:] if i < pivot])
		right = self.quickSort([i for i in array[1:] if i >= pivot])
		return left + [pivot] + right

	'''
      找出第k小的数

      没有必要对所有数进行排序，采用部分排序的方法
      1、对选择排序进行构造
      2、堆排序进行k趟排序

	'''
	def findSmallK(self, array,low, high, k):
		'''
           减少一半的工作量
		'''
		i = low
		j = high
		pivot = array[i]
		while i < j:
			while i < j and array[j] >= pivot:
				j -= 1
			if i < j:
				array[i] = array[j]
				i += 1
			while i < j and array[i] <= pivot:
				i += 1
			if i < j:
				array[j] = array[i]
				j -= 1
			array[i] = pivot
			split_index = i - low
			if split_index == k - 1:
				return array[i]
			elif split_index > k - 1:
				return self.findSmallK(array, low, i -1, k)
			else:
				return self.findSmallK(array, i + 1, high, k - (i - low) - 1)

             
print(Solution().quickSort([4,3,2,7,8,5]))

class Solution1:
	def minDistance(self, array, num1, num2):
		if not array or len(array) <= 0:
			return
		lastPos1 = -1
		lastPos2 = -1
		mindist = 2 ** 30
		i = 0
		while i < len(array):
			if array[i] == num1:
				lastPos1 = i
				if lastPos2 >= 0:
					mindist = min(mindist, lastPos1 - lastPos2)
			if array[i] == num2:
				lastPos2 = i
				if lastPos1 >= 0:
					mindist = min(mindist, lastPos2 - lastPos1)
			i += 1

		return mindist

print(Solution1().minDistance([4, 5, 6, 4,7, 4, 6, 4, 7, 8, 5, 6, 4, 3, 10, 8], 4, 8)) 

class Solution2:
	def findMin(self, array):
		'''
         在一个升序的数组当中，判断一个最小的绝对值的数
		'''
		if not array or len(array) <= 0:
			return 0
		lens = len(array)
		# 判断数组是否都是大于0
		if array[0] >= 0:
			return array[0]
		# 判断数组是否都是小于0
		if array[lens -1] <= 0:
			return array[lens-1]
		# 找出分界点，进行比较
		mid = 0
		low = 0
		end = lens - 1
		absmin = 0
		while True:
			mid = low + (end - low) >> 1
			if array[mid] == 0:
				return array[mid]
			elif array[mid] > 0:
				# 继续数组的左部分查找
				if array[mid - 1] == 0:
					return 0
				if array[mid -1] > 0:
					end = mid -1
				else:
					break
			else:
				if array[mid + 1] == 0:
					return 0
				if array[mid + 1] < 0:
					low = mid + 1
				else:
					break
		# 处理分界
		if array[mid] > 0:
			if array[mid] < abs(array[mid -1]):
				absmin = array[mid]
			else:
				absmin = abs(array[mid- 1])
		else:
			absmin = abs(array[mid]) if abs(array[mid] < array[mid + 1]) else array[mid +1]
		return absmin
print(Solution2().findMin([-10, -5, -2, 7, 15, 50]))

class Solution3:
	def maxSubarray(self, array):
		if not array or len(array) < 1:
			return
		cur_sum = array[0]
		max_sum = - 2 ** 32
		for i in array[1:]:
			cur_sum += i
			if cur_sum > max_sum:
				max_sum = cur_sum
			if cur_sum < 0:
				cur_sum = 0
		return max_sum

print(Solution3().maxSubarray([1, -2, 4, 8, -4, 7, -1, -5]))



			
