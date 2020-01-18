'''
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
A:
如果两个指针分别指向数字1和数字2，并设为small 和 big
求和，如果大于sum，删除small，并将small +1
如果小于small ，则把big加1，如果等于目标值，则输出small和big的序列，同时将big加1
继续操作
注意相等的情形指针依然需要移动，否则就会陷入死循环
'''
class Solution:
	def FindContinousSequence(self, tsum):
		small, big, res = 1, 2, []
		current_sum = small + big
		while small < big:
			if current_sum < tsum:
				big += 1
				current_sum += big
			else:
				if current_sum == tsum:
					res.append([i for i in range(small, big + 1)])
				current_sum -= small
				small += 1
			
		return res


		'''
		输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
		如果有多对数字的和等于S，输出两个数的乘积最小的。
		A: 两个指针，一个指向起点，一个指向终点，然后对两个数字求和，如果大于S，则向前移动一个
		指针，否者把另一个指针向后移动
		'''
	def FindNumberWithSum(self, array, tsum):
		if not array or not tsum:
			return []
		start = 0
		end = len(array) - 1
		while start < end:
			current_sum = array[start]  + array[end]
			if current_sum < tsum:
				start += 1
			elif current_sum > tsum:
				end -= 1
			else:
				return [array[start], array[end]]
		return []
		