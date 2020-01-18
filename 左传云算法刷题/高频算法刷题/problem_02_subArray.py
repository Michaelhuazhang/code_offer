# -*- encoding:utf-8 -*-

# Q:在一个数组中都是正数，判断这个数组中子数组和为k的最长长度
# Q2:在一个数组中正负都有，判断这个数组中子数组和为k的最长子数组长度
# Q3:在一个数组中正负都有，寻找一个数组中子数组和<=k 的最长子数组长度

'''
  A1:两个指针滑动，求出以每个元素开头的最长子数组。利用数组之和递增
  A2：以每一个元素结尾的最长子数组，要求出最长的，求出这个数组累加最早到sum-k，其区间就是长度
  A3：需要辅助结构，和小于K，当以每个元素开头向后=累加最小和若大于K，则以这个元素开头无法存在一个子数组和小于K
    若这个元素开头累加和小于K，观察下一个位置，两者的和若>k,说明下一个位置无法再次加入
    若依旧小于，则继续过程。
    当遍历下一个元素的时候，能够利用当前的和-上一个元素的和，加速操作

'''
class Solution:
	def getMaxlengthInPositive(self, array, k):
		if not array or len(array) == 0 or k <= 0:
			return 0
		left = 0
		right = 0
		temp_sum = array[0]
		lens = 0
		while right < len(array):
			if temp_sum == k:
				lens = max(lens, right - left + 1)
				# 左指针向右滑动
				left += 1
				temp_sum -= array[left]
			elif temp_sum < k:
				right += 1
				if right == len(array):
					break
				temp_sum += array[right]
			else:
				left += 1
				temp_sum -= array[left]
		return lens

	def getmaxlength(self, array, k):
		if not array or len(array) == 0:
			return 0
		dicts = {0: -1}
		lens = 0
		temp_sum = 0
		for i in range(len(array)):
			temp_sum += array[i]
			if (temp_sum - k) in dicts:
				lens = max(lens, i - dicts[temp_sum-k])
			if (temp_sum) not in dicts:
				dicts[temp_sum] = i
		return lens

	def maxlengthAweSome(self, array, k):
		if not array or len(array) == 0:
			return 0
		sums = [0 for i in range(len(array))]
		ends = {}
		sums[len(array) - 1] = array[len(array) - 1]
		ends[len(array) - 1] = len(array) - 1
		for i in range(len(array)-2, -1, -1):
			if sums[i+1] < 0:
				sums[i] = array[i] + sums[i+1]
				ends[i] = ends[i+1]
			else:
				sums[i] = array[i]
				ends[i] = i
		end = 0
		sumarray = 0
		res = 0
		for i  in range(len(array)):
			while end < len(array) and sumarray + sums[end] <= k:
				sumarray += sums[end]
				end = ends[end] + 1
			sumarray -= array[i] if end > i else 0
			res = max(res, end - i)
			end = max(end, i+1)
		return res

print(Solution().maxlengthAweSome([1, 7, 9, -5, -4, 3, 2, 4, -4, 2], 7))
print(Solution().getMaxlengthInPositive([1, 2, 3, 4, 5, 2, 3, 1, 1, 2, 4], 7))
print(Solution().getmaxlength([-2, -1, 3, 4, 2, 3,1], 4))
