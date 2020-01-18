# -*- encoding:utf-8 -*-
print("zjh")


class Solution:
	def mergeSort(self, array):
		if not array or len(array) < 2:
			return array
		mid = int(len(array) / 2)

		left = self.mergeSort(array[:mid])
		right = self.mergeSort(array[mid:])
		return self.merge(left, right)


	def merge(self,  left,  right):
		c = []
		l = r = 0
		while l < len(left) and r < len(right):
			if left[l] < right[r]:
				c.append(left[l])
				l += 1
			else:
				c.append(right[r])
				r += 1
		if l == len(left):
			for i in right[r:]:
				c.append(i)
		else:
			for i in left[l:]:
				c.append(i)
		return c


array = [1, 4, 2, 7, 3, 9]
print(len(array) / 2)
print(len(array))
print(Solution().mergeSort([1, 4, 2, 7, 3, 9]))