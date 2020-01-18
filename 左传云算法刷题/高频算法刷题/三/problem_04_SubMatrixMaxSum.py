# -*- encoding:utf-8 -*-
# Q:求出矩阵中，其值有正有负，返回子矩阵最大累加和
# 一个矩阵中的子矩阵为n6次方
# 一个矩阵中的子矩阵为正方形，起点n平方*边长n

# 先求第一行为底的最大子矩阵和
# 然后求第二行为底。。。。。
import sys

class Solution:
	def maxSum(self, array):
		if not array or len(array) == 0 or len(array[0]) == 0:
			return 0
		maxSum = -sys.maxsize
		cur = 0
		
		for i in range(len(array)):
			# 辅助累加数组
			help_sum = [0 for x in range(len(array[0]))]
			# 控制行到j行
			for j in range(i, len(array)):
				cur = 0
				# 累加每列的数
				for k in range(len(help_sum)):
					help_sum[k] += array[j][k]
					cur += help_sum[k]
					maxSum = max(maxSum, cur)
					cur = 0 if cur < 0 else cur
		return maxSum

print(Solution().maxSum([[-90, 48, 78], [64, -40, 64], [-81, -7, 66]]))



