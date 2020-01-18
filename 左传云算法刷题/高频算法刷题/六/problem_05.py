# -*- encoding:utf-8 -*-

# K分钟走到T， 一开始在P位置


class Solution:
	def f1(self, n, k, p, t):
		if n < 2 or p < 0 or p >=n or k <1 or t<0 or t >=n:
			return 0
		if k == 1:
			return 1 if t == p else 0
		if t == 0:
			return self.f1(n, k-1, t+1, p)
		if t == n-1:
			return self.f1(n, k-1, t-1, p)
		return self.f1(n, k-1, t-1, p) + self.f1(n, k-1, t+1, p)