# -*- encoding:utf-8 -*-
# 如果一个数组中的最大值-最小值<= k
# 则这个数组中所有的子数组都满足

# 但如果一个数组已经不满足最大值-最小值 <= k,再扩肯定不满足

# 得到一个滑动窗口中的最大值和最小值

# 窗口内最大值为双端队列的头部， 最小值为双端队列的右边
# 更新L，看是否过期
# 当前的数确保
# 需要两个窗口最大值最小值更新结构

# 两个指针，，LR滑动，等同每个元素开头有多少子数组

from collections import deque

class Solution:
	def getNum(self, array, num):
		if not array or len(array) == 0:
			return 0
		qmin = []
		qmax = []
		left = 0
		right = 0
		res = 0
		while left < len(array):
			while right < len(array):#左右指针滑动窗口中间
				while len(qmin) != 0 and array[qmin[-1]] >= array[right]:
					# 需要弹出当前队列尾部
					qmin.pop()
				qmin.append(right)
				while len(qmax) != 0 and array[qmax[-1]] <= array[right]:
					# 需要弹出当前尾部
					qmax.pop()
				qmax.append(right)
				if array[qmax[0]] - array[qmin[0]] > num:
					break
				right += 1
			if qmin[0] == left:
				# 判断当前过期
				qmin.pop(0)
			if qmax[0] == left:
				qmax.pop(0)
			res += right - left
			left += 1
		return res
print(Solution().getNum([1, 2, 5, 3, 7, 2, 5, 3, 9, 10], 1))


