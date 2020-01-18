# -*- encoding:utf-8 -*-

class Solution:
	def getsmallSum(self, array):
		if not array or len(array) == 0:
			return 0
		return self.func(array, 0, len(array) - 1)

	def func(self, array, left, right):
		if (left == right):
			return 0
		mid = (left + right) // 2
		return self.func(array, left, mid) + self.func(array, mid + 1, right) + self.merge(array, left, mid, right)

	def merge(self, array, left, mid, right):
		temp_array = [0 for i in range(right-left + 1)]
		t_i = 0
		i = left
		j = mid+1
		small_sum = 0
		while i <= mid and j <= right :
			if array[i] <= array[j]:
				small_sum += array[i] * (right - j + 1)
				temp_array[t_i] = array[i]
				t_i += 1
				i += 1
			else:
				temp_array[t_i] = array[j]
				t_i += 1
				j += 1
		while i <= mid or j <= right:
			temp_array[t_i] = array[i] if i <= mid else array[j]
			t_i +=1
			i += 1
			j += 1
		for i in range(len(temp_array)):
			array[left] = temp_array[i]
			left += 1
		return small_sum

print(Solution().getsmallSum([2, 1, 2, 2,3]))
print(Solution().getsmallSum([1, 3, 5, 2, 4, 6]))