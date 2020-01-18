# -*- encoding:utf-8 -*-

# 最长递增子序列（可以不连续）
# 一个辅助数组，必须以每一个元素结尾的最长递增子序列

# 当前数的前面比该数小，前面的数的最长递增子序列 + 1
# 左边信息帮助右边加速
# 返回这个子序列，利用信息进行回归


# 最小结尾数组
# 遍历当前元素为止，长度为i+1的所以递增子序列，最小结尾是3


# class Solution:
# 	def getlongestSubSeries(self, array):
n = 10
for i in range(n):
	print(~i)