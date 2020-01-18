# -*- encoding:utf-8 -*-


class Solution:

	# 滑动数组中最大值返回

	def getMaxWindow(self, array, w):
		if not array or len(array) < w or w <= 0:
			return []

		array_queue = [] # 存放的是index
		res = [-1 for i in range(len(array) - w + 1)] # 目标结果
		index = 0 # 索引
		for i in range(len(array)):
			while len(array_queue) != 0 and array[array_queue[-1]] <= array[i]:
				array_queue.pop()
		    # 加入
			array_queue.append(i)
			# 满足过期，则弹出第一个
			if (array_queue[0] == i - w):
				array_queue.pop(0)
			# 将当前滑动窗口能够填充值
			if i >= w -1:
				res[index] = array[array_queue[0]]
				index += 1
		return res

	def getNum(self, array, num):
		'''
          判断子数组的最大值减去最小值小于等于num的个数

		'''
		if not array or len(array) == 0:
			return 0
		max_array = []
		min_array = []
		left, right, res = 0
		while left < len(array):
			while right < len(array):
				while len(min_array) != 0 and array[min_array[-1]] >= array[right]:
					min_array.pop()

			    min_array.append(right)
			    while len(max_array) != 0 and array[max_array[-1] <= array[right]]:
			    	max_array.pop()

			    max_array.append(right)
			    if (array[max_array[0]] - array[min_array[0]]) > num:
			    	break
			    right += 1

			if (min_array[0] == left):
				min_array.pop(0)
			if max_array[0] == left:
				max_array.pop(0)
			res += right - left
			left += 1
		return res
		

			
print(Solution().getMaxWindow([2, 3, 4, 2, 6, 2, 5, 1], 3))



