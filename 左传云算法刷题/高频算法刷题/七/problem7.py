# -*- encoding:utf-8 -*-
# import heapq

# lists = [1,8,2,23,7,-4,18,23,42,37,2]
# print(heapq.nlargest(1, lists))
# print(heapq.nsmallest(1, lists))


# heapq.heapify(lists)
# a = heapq.heappop(lists)
# print(a)
# b = heapq.heappop(lists)
# print(b)
from heapq import *
a = [1,8,2,23,7,-4,18,23,42,37,2]
# heapify(a)
# print(a)
# print(heappop(a))
# heappush(a, -30)
# print(heappop(a))
# print(nsmallest(3, a))
# print(nlargest(1, a))
# print(heapreplace(a, -60))
# print(heappop(a))
# print(len(a))

class Solution:
	def lessMoney(self, array):
		if not array or len(array) == 0:
			return 0
		heapify(array)
		sums = 0
		cur = 0
		while len(array) > 1:
			cur = heappop(array) + heappop(array)
			sums += cur
			heappush(array, cur)
		return sums

print(Solution().lessMoney([6, 7, 8, 9]))