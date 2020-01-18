# -*- encoding:utf-8 -*-
# Q: 给定一个二维数组，求出其中练成一片的岛的个数


class Solution:
	def countsIslands(self, array):
		if not array or not array[0] :
			return 0
		N = len(array)
		M = len(array[0])
		res = 0
		for i in range(N):
			for j in range(M):
				if array[i][j] == 1:
					res += 1
					self.infect(array, i, j, N, M)
		return res

	def infect(self, array, i, j, N, M):
		if i < 0 or i >= N or j < 0 or j >= M or array[i][j] != 1 :
			return 0
		array[i][j] = 2 # 已感染的转化为2
		self.infect(array, i+1, j, N, M)
		self.infect(array, i-1, j, N, M)
		self.infect(array, i, j+1, N, M)
		self.infect(array, i, j-1, N, M)

array = [[1 for i in range(5)] for j in range(5)]
print(Solution().countsIslands(array))
