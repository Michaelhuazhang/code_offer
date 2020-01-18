# -*- encoding:utf-8 -*-
'''
A:求数组之间补水高度之和多少
转换为每个元素上补水的高度 == min（max（左侧）， max(右侧)）

'''
'''
     解决方法1最主要的问题在于每次遍历都要在两侧寻找最大值
     应对方法：保存元素左右最大值
'''

class Solution:
	def getWater1(self, array):
		if not array or len(array) < 3:
			return 0
		value = 0
		for i in range(1, len(array) - 1):
			leftmax = 0
			rightmax = 0
			for l in range(i):
				leftmax = max(leftmax, array[l])
			for r in range(i+1, len(array)):
				rightmax = max(rightmax, array[r])
			# 遍历得到元素左右最大值
			value += max(0, min(rightmax, leftmax) - array[i])
		return value
    
	def getWater2(self, array):

		if not array or len(array) < 3:
			return 0
		lens = len(array) - 2
		leftmaxs = [0 for i in range(lens)]
		leftmaxs[0] = array[0]
		for i in range(1, lens):
			leftmaxs[i] = max(leftmaxs[i-1], array[i])
		rightmaxs = [0 for i in range(lens)]
		rightmaxs[lens - 1] = array[lens +1]
		for i in range(lens-2, -1, -1):
			rightmaxs[i] = max(rightmaxs[i+1], array[i+2])
		value = 0
		for i in range(1, lens + 1):
			value += max(0, min(leftmaxs[i-1], rightmaxs[i-1]) - array[i])
		return value

	def getWater3(self, array):
		'''
        加速，将左边最大加速到得出结果中
		'''
		if not array or len(array) < 3:
			return 0
		n = len(array) - 2
		rightmaxs = [0 for i in range(n)]
		rightmaxs[n-1] = array[n+1]
		for i in range(n-2, -1, -1):
			rightmaxs[i] = max(rightmaxs[i+1], array[i+2])
		leftmax = array[0]
		value = 0
		for i in range(1, n+1):
			value += max(0, min(leftmax, rightmaxs[i-1]) - array[i])
			leftmax = max(leftmax, array[i])
		return value

	def getWater4(self, array):
		if not array or len(array) < 3 :
			return 0
		value = 0
		leftmax = array[0]
		rightmax = array[len(array) - 1]
		l = 1
		r = len(array) - 2
		while l <= r:
			if leftmax <= rightmax:
				value += max(0, leftmax- array[l])
				leftmax = max(leftmax, array[l])
				l += 1
			else:
				value += max(0, rightmax - array[r])
				rightmax = max(rightmax, array[r])
				r -= 1
		return value

print(Solution().getWater1([4, 7, 5, 2, 1, 3, 5, 9]))

print(Solution().getWater2([4, 7, 5, 2, 1, 3, 5, 9]))

print(Solution().getWater3([4, 7, 5, 2, 1, 3, 5, 9]))
print(Solution().getWater4([4, 7, 5, 2, 1, 3, 5, 9]))
