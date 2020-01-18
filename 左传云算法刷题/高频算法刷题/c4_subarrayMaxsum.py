# -*- encoding:utf-8 -*-


class Solution:
	def maxSum(self, array):
		'''
        返回最大子数组和

        以每一个元素结尾的最大子数组之和。
        更新策略：累加和为负数，归为0
        不可能最大子数组和的前缀为负数
		'''
		if not array or len(array) == 0:
			return 0
		maxSum = array[0]
		curSum = 0
		for i in array:
			curSum += i
			maxSum = max(maxSum, curSum)
			curSum = 0 if curSum < 0 else curSum
		return maxSum


array1 = [-2, -3, -5, 40, -10, -10, 100, 1 ]
array2 = [-2, -3, -5, 0, 1, 2, -1]
array3 = [-2, -3, -5, -1]



print(Solution().maxSum(array1))
print("the  max sum of sub array in array2 is %d "%(Solution().maxSum(array2)))
print("the  max sum of sub array in array3 is %d "%(Solution().maxSum(array3)))