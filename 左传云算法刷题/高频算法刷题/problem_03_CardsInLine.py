# -*- encoding:utf-8 -*-

# Q:给出一堆纸牌，两个人轮流交替拿，返回最大的那个和

class Solution:
	def firstget(self, array, i, j):
		'''
         i，j代表数组的边界
		'''
		if i == j:
			return array[i]
		return max(array[i] + self.secondget(array, i+1, j), array[j] + self.secondget(array, i, j-1))

	def secondget(self, array, i, j):
		if i == j:
			return 0
		return min(self.firstget(array, i+1, j), self.firstget(array, i, j-1)) 

	def win1(self, array):
		if not array or len(array) == 0:
			return 0
		sums = sum(array)
		ones = self.firstget(array, 0, len(array) - 1)
		return max(ones, sums - ones)
		# return max(self.firstget(array, 0, len(array) - 1), self.secondget(array, 0, len(array) - 1))

	def allprocess(self, array, i, j):
		if i == j:# 只含有一个元素
			return array[i]
		if i + 1 == j:# 含有两个元素
			return max(array[i], array[j])
		return max(array[i] + min(self.allprocess(array, i+1, j-1), self.allprocess(array, i+2, j)) ,
		          array[j] + min(self.allprocess(array, i+1, j-1), self.allprocess(array, i, j-2)))


	def win2(self, array):
		if not array or len(array) == 0:
			return 0
		sums = sum(array)
		a = self.allprocess(array, 0, len(array) - 1)
		return max(a, sums - a)
	
	def win3(self, array):
		'''
            动态归化，由方法1转化得到
            
		'''
	def win4(self, array):
		if not array or len(array) == 0:
			return 0
		if len(array) == 1:
			return array[0]
		if len(array) == 2:
			return max(array[0], array[1])
		sums = sum(array)
		dp = [[0 for i in range(len(array))] for j in range(len(array))]
		for i in range(len(array) -1):
			dp[i][i] = array[i]
			dp[i][i+1] = max(array[i], array[i+1])
		dp[len(array) -1][len(array)-1] = array[-1]

		for k in range(2, len(array)):
			for j in range(k, len(array)):
				i = j - k
				dp[i][j] = max(array[i] + min(dp[i+2][j], dp[i+1][j-1]),
					array[j] + min(dp[i+1][j-1], dp[i][j-2]))
		return max(dp[0][len(array)-1], sums - dp[0][len(array) - 1])
array = [12, 23, 45, 56]
print(Solution().win1(array))
print(Solution().win2(array))
print(Solution().win4(array))
