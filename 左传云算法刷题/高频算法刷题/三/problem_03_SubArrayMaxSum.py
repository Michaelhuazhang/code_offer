# -*- encoding:utf-8 -*-

# Q: 求出数组中的最大子树组的和是多少
# 最大子树组的和的前缀一定不是负数



# 在一个数组中最大的子数组的乘积
# 目标结算以每一个数结尾的最大乘积 
# 当前i *i-1最大乘积
# i-1最小*当前i
# 只是当前i
# 只有上述三种情况
# a 记录最大，b记录最小

import sys
class Solution:
	def maxSum(self, array):
		if not array or len(array) == 0:
			return 0
		maxSum =  -sys.maxsize
		cur_sum = 0
		for i in array:
			cur_sum += i
			maxSum = max(maxSum, cur_sum)
			cur_sum = 0 if cur_sum < 0 else cur_sum   # 淘汰不可能的子数组,尝试可能的前缀

		return maxSum

	def maxMultiply(self, array):
		if not array or len(array) == 0:
			return 0
		min_multi = array[0]
		max_multi = array[0]
		max_m = array[0]
		for i in array[1:]:
			end1 = max_multi * i
			end2 = min_multi * i
			max_multi = max(max(end1, end2), i)
			min_multi = min(min(end1, end2), i)
			max_m = max(max_m, max_multi)
		return max_m
array1 = [-2, -3, -5, 40, -10, -10, 100, 1 ]
print(Solution().maxSum(array1))
print(Solution().maxMultiply(array1))
print("zjh")