# -*- encoding:utf-8 -*-
# Q: 给定一个数组，左右两部分最大值的差的绝对值最大是多少
# A: 遍历每一个元素划分，，左右最大相减，更新最大
# AweSome： 数组最大的元素无论是在左右两边，肯定是一测最大，那么另一侧最大肯定包括开头第一个元素或者结尾元素
# 要想这一侧元素最大最小，则不能更新，否则这侧的最大值将要变大
import sys
class Solution:
	def maxAbs(self, array):
		if not array or len(array) < 2:
			return 0
		res = -sys.maxsize
		maxleft = 0
		maxright = 0
		for i in range(len(array)-1):
			# 每次遍历过程中，求出两侧最大
			maxleft = -sys.maxsize
			for j in range(i+1):
				maxleft = max(maxleft, array[j])
			maxright = -sys.maxsize
			for j in range(i+1, len(array)):
				maxright = max(maxright, array[j])
			res = max(res, abs(maxleft - maxright))
		return res

	# 每次遍历都需要找到左右最大==>保存记录最大

	def maxAbs1(self, array):
		if not array or len(array) < 2:
			return 0
		la = [0 for i in array]
		ra = [0 for i in array]
		la[0] = array[0]
		ra[len(array)-1] = array[-1]
		for i in range(1, len(array)):
			la[i] = max(la[i-1], array[i])
		for j in range(len(array)-2, -1, -1):
			ra[j] = max(ra[j+1], array[j])
		maxabs = 0
		for i in range(len(array)-1):
			maxabs = max(maxabs, abs(la[i]-ra[i+1]))
		return maxabs

	def getmaxabs(self, array):
		if not array or len(array) < 2:
			return 0
		res = -sys.maxsize
		maxnum = -sys.maxsize
		for i in array:
			maxnum = max(maxnum, i)
		return maxnum - min(array[0], array[-1])

print(Solution().maxAbs([45, 23, 78, 12, 23, 98, 11]))
print(Solution().maxAbs1([45, 23, 78, 12, 23, 98, 11]))
print(Solution().getmaxabs([45, 23, 78, 12, 23, 98, 11]))
