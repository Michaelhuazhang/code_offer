# -*- encoding:utf-8 -*-
'''
 在都是正数的数组当中，返回其子数组和等于k的最长子数组长度

 A:左右两个指针进行滑动，记录长度，比较最长数组
'''

class Solution:
	def getMaxLength(self, array, k):
		if not array or len(array) == 0 or k <= 0:
			return 0
		left = 0
		right = 0
		sums = array[0]
		maxlen = 0
		while right < len(array):
			if sums == k:
				maxlen = max(maxlen, right - left + 1)
				sums -= array[left]# 左指针继续滑动，和减少
				left += 1
			elif sums < k:# 小于K，右边指针移动
				right += 1
				if right == len(array):
					break# 注意越界
				sums += array[right]
			else:
				sums -= array[left]
				left += 1
		return maxlen

print(Solution().getMaxLength([3, 1, 1, 1, 4, 3, 2, 2, 3], 7))
