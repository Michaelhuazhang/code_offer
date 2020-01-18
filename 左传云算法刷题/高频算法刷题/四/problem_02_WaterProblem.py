# -*- encoding:utf-8 -*-

# Q：给定一个数组，每个值代表一个高度，那这个数组可以看出一个直方图，直方图当成容器
# A: 问题转化为每一个值上能留多少水为   最小值（左边整体的最大值和右边整体最大的值的）
# 1、两边元素不可能有水（1， n-2）
# 左右指针，左右最大
# 左边最大小于右边最大，可以计算（关心最小的）

class Solution:
	# 暴力求出左右整体最大值，复杂度n方
	def getWater1(self, array):
		if not array or len(array) < 3:
			return 0
		value = 0
		for i in range(1, len(array)-1):
			leftmax = 0
			rightmax = 0
			for l in range(i):
				leftmax = max(array[l], leftmax)
			for r in range(i+1, len(array)):
				rightmax = max(array[r], rightmax)
			value += max(0, min(rightmax, leftmax) - array[i])
		return value

	# 保留，预处理左右最大值
	def getwater2(self, array):
		if not array or len(array) < 3:
			return 0
		value = 0
		n = len(array) - 2
		leftmaxs = [0 for i in range(n)]
		rightmax = [0 for i in range(n)]
		leftmaxs[0] = array[0]
		for i in range(1, n):
			leftmaxs[i] = max(leftmaxs[i-1], array[i])
		rightmax[n-1] =array[-1]
		for j in range(n-2, -1, -1):
			rightmax[j] = max(rightmax[j+1], array[j+2])
		for i in range(1, n+1):
			value += max(0, min(leftmaxs[i-1], rightmax[i-1]) - array[i])
		return value

	def getWater(self, array):
		if not array or len(array) < 3:
			return 0
		value = 0
		leftmax = array[0]
		rightmax = array[-1]
		# 左右指针滑动
		left = 1
		right = len(array) - 2
		while left <= right:
			if leftmax <= rightmax:# 关心最小的 进行计算
				value += max(0, leftmax - array[left])
				leftmax = max(leftmax, array[left])
				left += 1
			else:
				value += max(0, rightmax - array[right])
				rightmax = max(rightmax, array[right])
				right -= 1
		return value
array = [ 5, 1, 2, 4, 3, 8, 9, 2, 14]
print(Solution().getWater1(array))
print(Solution().getwater2(array))
print(Solution().getWater(array))


