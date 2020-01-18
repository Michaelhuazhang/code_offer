# -*- encoding:utf-8 -*-
# Q:求不重叠子数组异或为0的个数最多
# 求每个元素结尾并且最后一块异或结果以该元素结尾

# 异或满足交换律和结合律

# 从0-i异或的结果为某一个数，然后从o异或到中间每一个数异或的结果
# 查找相等的时候，找最近的
# 当前结尾元素i：当前i能不能找到以i结尾异或出0的，若能，则在之前的个数+1，负责，复用i-1的个数
# 记录每个元素异或的结果放入map中，不存在，保存，存在，则更新

##################################################################################################
# 找到一个数组累加和为K的最长的子数组
# 首先累加每一个元素的和，找到以当前元素结尾累加和为K，sum-k最早出现的位置
# sum 放一个map中
# map中要存放0，，-1的键值对，因为是j+1~i
# 避免错过第一个元素

##################################################################################################
# 一个数组中全是正数，求累加和最长为k的子数组
# 双指针滑动，右指针滑动，累加和等于k，返回，然后，less++
# 若大于k，less++,若小于k，则left++
# 计算以每一个元素开头累加和为k的最长子数组


##################################################################################################
# 一个数组中累加和小于K的最长子数组
# 记录每一个元素向后最小累加和
# 若一个元素向后累加最小和都不满足小于K，则以该元素开头一定不会产生数组
# 小于k，则计算向后累加和下一个位置累加和+该元素最小累加和是否小于K，若小于，继续
# 否则，就是之前的位置，然后用sum-开头元素，为下一个位置累加和，进行加速，如果不能，再进行下一个元素
# 至于中间产生的不是我们不关心的大小，我要最长的，就是是否就是继续能扩下去



# 必须以每一个元素开头最小累加和
# 最小累加和的index
# 从右往前遍历
# 就是之前元素累加和为负，相加，不然，就是自己
# 相加，则为之前的index，否则就是自己的index

##################################################################################################
# 一个数组中最大累加和
# 扩展到二维数组中求最大累加和

# 最大累加和的前缀一定不是负数，若是负数，我就没有必要加上负数

# 那么cur记录当前累加和，cur若变化为负，更新
# 最大记录就是比较cur的最大值
# 返回最大值

##################################################################################################
# 扩展到二维数组中求最大累加和，子矩阵
# 求每一行开头，往下的子矩阵
# 划为上述过程
# 复用help数组，加速，加上一行的help加当前行的元素
from heapq import *
import sys

class Solution:
	def getMaxlengthinPositiveArray(self, array, k):
		if not array or len(array) == 0 or k <= 0:
			return 0
		left = 0
		right = 0
		lens = 0
		sums = array[0]
		while right < len(array):
			if sums == k:
				lens = max(lens, right - left + 1)
				sums -= array[left]
				left += 1
			elif sums < k:
				right += 1
				if right == len(array):
					break
				sums += array[right]
			else:
				sums -= array[left]
				left += 1
		return lens

	def getMaxlengthInArray(self, array, k):
		if not array or len(array) == 0:
			return 0
		dicts = {0:-1}
		lens = 0
		cursum = 0
		for i in range(len(array)):
			cursum += array[i]
			if cursum - k in dicts:
				lens = max(lens, i - dicts[cursum - k])
			if cursum not in dicts:
				dicts[cursum] = i
		return lens

	def getMaxlengthlessKInArray(self, array, k):
		if not array or len(array) == 0:
			return 0
		# 定义最小累加和和最小累加和前缀
		leastsums = [0 for i in range(len(array))]
		ends = {}
		leastsums[len(array) - 1] = array[-1]
		ends[len(array)-1] = len(array) - 1
		for i in range(len(array)-2, -1 , -1):
			if leastsums[i+1] < 0:
				leastsums[i] = array[i] + leastsums[i+1]
				ends[i] = ends[i+1]
			else:
				ends[i] = i
				sums[i] = array[i]

		res = 0
		sums = 0
		end = 0
		for i in range(len(array)):
			while end < len(array) and leastsums[end] + sums <= k:
				sums += leastsums[end]
				end += ends[end] + 1
			#b下一轮的sums
			sums -= array[i] if end > i else  0
			# 记录长度
			res = max(res, end - i)
			# 
			end = max(end, i + 1)
		return res

	def mostXor(self, array):
		if not array or len(array) == 0:
			return 0
		ans = -sys.maxsize
		xor = 0
		mosts = [0 for i in len(array)]
		maps = {0:-1}
		for i in range(len(array)):
			xor ^= array[i]
			if xor in maps:
				pre = maps[xor]
				mosts[i] = 1 if pre == -1 else mosts[pre] + 1
			if i > 0:
				mosts[i] = max(mosts[i-1], mosts[i])
			maps[xor] = i
			ans = max(ans, mosts[i])
		return ans

	def maxSum(self, array):
		if not array or len(array):
			return 0
		cursum = 0
		res = 0
		maxs = -sys.maxsize
		for i in array:
			cursum += i
			maxs = max(maxs, cursum)
			cursum = 0 if cursum < 0 else cursum
		return maxs

	def maxSumsubMatrix(self, array):
		if not array or len(array) == 0 or len(array[0]):
			return 0
		maxs = - sys.maxsize
		curs = 0
		for i in range(len(array)):
			helps = [0 for i in range(len(array[0]))]
			for j in range(i, len(array)):
				curs = 0
				for k in range(len(array[0])):
					# 更新数组
					helps[k] += array[j][k]
					# 更新当前累加和
					curs += helps[k]
					# 更新最大值
					maxs = max(maxs, curs)
					# 更新前缀和
					curs = 0 if curs < 0 else curs
		return maxs

	def uglyNumber(self, n):
		helps = [0 for i in range(n)]
		helps[0] = 1
		i2 = 0
		i3 = 0
		i5 = 0
		index = 1
		while index < n:
			helps[index] = min(2 * helps[i2], min(3 * helps[i3], 5 * helps[i5]))
			if helps[index] == 2 * helps[i2]:
				i2 += 1
			if helps[index] == 3 * helps[i3]:
				i3 += 1
			if helps[index] == 5 * helps[i5]:
				i5 += 1
			index += 1
		return helps[index - 1]

	def getMinKNumsByHeap(self, array, k):
	 	if not array or len(array) == 0 or k < 0:
	 		return None
	 	helps = []
	 	for i in array[:k]:
	 		helps.append(i)
	 	heapify(helps)
	 	for i in range(k, len(array) - 1):
	 		if array[i] < array[0]:
	 			heapreplace(helps, array[i])
	 	return helps

print(Solution().getMinKNumsByHeap([1, 2, 21, 12,45], 5))






print(Solution().getMaxlengthinPositiveArray([1, 2, 3, 1, 7], 7))
print(Solution().getMaxlengthInArray([1, -1, 1, -1, 4, 2, 2], 4))