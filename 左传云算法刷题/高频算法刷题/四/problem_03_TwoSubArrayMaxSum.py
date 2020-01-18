# -*- encoding:utf-8 -*-

# Q: 一个数组中两个不相交的子数组最大和
# 找出每个元素坐标最大字数和和右边最大子树组的和
import sys
class Solution:
	def twoSubArray(self, array):
		if not array or len(array) < 2:
			return 0
		rArray = [0 for i in array]
		maxs = -sys.maxsize
		cur = 0
		for i in range(len(array) - 1, -1, -1):
			cur += array[i]
			maxs = max(maxs, cur)
			rArray[i] = maxs
			cur = 0 if cur < 0 else cur
		res = -sys.maxsize
		maxs = -sys.maxsize
		cur = 0
		# 左边最大子数组和，在遍历中生成
		for i in range(len(array)-1):
			cur += array[i]
			maxs = max(maxs, cur)
			res = max(res, maxs + rArray[i+1])
			cur = 0 if cur < 0 else cur
		return res


