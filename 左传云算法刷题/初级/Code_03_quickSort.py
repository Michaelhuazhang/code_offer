# -*- encoding:utf-8 -*-
# 快排的原理就是基于分治策略，设定一个基准线pivot，将数据分为两部分
# 不断实现数据的排序
# 时间复杂度nlgn，最差为n方，属于不稳定排序，空间复杂度为O（1）

# 非递归快排思路
# 利用栈的思想，需要继续排序的首尾下标存入栈中，不断弹栈进行区分操作

class Solution:
	def quickSort(self, array):
		if not array or len(array) == 0:
			return []
		else:
			pivot = array[0]
			left = self.quickSort([x for x in array[1:] if x < pivot])
			right = self.quickSort([x for x in array[1:] if x > pivot])
			return left + [pivot] + right


	def quick_sort_stack(self, array):
		if not array or len(array) == 0:
			return 0
		if len(array) < 2:
			return array
		stack = []
		# 先进右边后进左边
		stack.append(len(array) - 1)
		stack.append(0)
		while len(stack) != 0:
			l = stack.pop() # 弹出首元素下标
			r = stack.pop() # 弹出尾元素下标
			index = self.partition(array, l, r)
			if l < index - 1:
				stack.append(index-1)
				stack.append(l)
			if r > index + 1:
				stack.append(r)
				stack.append(index+1)
			
		return array

	def partition(self, array, start, end):
		# 拿出基准
		pivot = array[start]
		while start < end:
			while start < end and array[end] >= pivot:
				end -= 1
			array[start] = array[end]
			while start < end and array[start] <= pivot:
				start += 1
			array[end] = array[start]
		array[start] = pivot
		# 返回基准元素的位置
		return start


class Solution1:
	def quickSort(self, array):
		if not array or len(array) < 2:
			return array
		self.quickSort1(array, 0, len(array)-1)

	def quickSort1(self, array, left, right):
		if left < right:
			p = self.partition(array, left, right)
			self.quickSort1(array, left, p-1)
			self.quickSort1(array, p+1, right)

	def partition(self, array, left, right):
		if left < right:
			pivot = array[left]
			while left < right:
				while right > left and array[right] > pivot:
					right -= 1

				array[left] = array[right]
				while left < right and array[left] < pivot:
					left += 1
				array[right] = array[left]
			array[left] = pivot
			return left

print(Solution().quickSort([1, 5, 2, 7, 9, 6]))



print(Solution().quick_sort_stack([1, 5, 2, 7, 9, 6,45, 21,2]))
array = [1, 5, 2, 7, 9, 6,45, 21,2]
print(array)
print(Solution1().quickSort(array))
print(array)