# -*- encoding:utf-8 -*-

class Solution:
	def firstget(self, array, i, j):
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
  		sums = 0
  		for i in array:
  			sums += i
  			first = self.firstget(array, 0, len(array))
  		return max(first, sums - first)

print(Solution().win1([4,7, 8, 9, 4], 0, 4)
# print("ZJH")