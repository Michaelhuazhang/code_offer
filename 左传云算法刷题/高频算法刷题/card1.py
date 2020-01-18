# -*- encoding:utf-8 -*-

class Solution:
	def win3(self, array):
		if not array or len(array) == 0:
			return 0
		sums = sum(array)
		scores = self.p(array, 0, len(array) - 1)
		return max(sums-scores, scores)

	def p(self, array, i, j):
		if i == j:
			return array[i]
		if i + 1 == j:
			return max(array[i], array[j])
		return max(array[i] + min(self.p(array, i+2, j), self.p(array, i+1, j-1)),
			array[j] + min(self.p(array, i+1, j-1), self.p(array,i, j-2)))

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

print(Solution().win3([4, 8, 56, 45, 78]))	
print(Solution().win4([4, 8, 56, 45, 78]))