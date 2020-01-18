# -*- encoding:utf-8 -*-

# Q:将a_i放入b序列的尾部
# 逆置序列
# 操作n次
# 1
# 21   12 逆
# 312  312 不逆
# 4213  3124 逆
# 先往右，后往左，交替添加，并交替逆序
# 双端队列实现

class Solution:
	def getfinal(self, n, array):
		convert = False
		deque = []
		for i in range(n):
			if convert:
				deque.append(array[i])
			else:
				deque.insert(0, array[i])
			convert = not convert
		if convert:
			print([deque[i] for i in range(len(array))])
		else:
			print([deque[i] for i in range(len(array)-1, -1, -1)])

Solution().getfinal(5, [1, 2, 3, 4, 5])


# n = int(raw_input(""))
# x = map(int, raw_input("").split(" "))
# y = map(int, raw_input("").split(" "))
# zips = zip(x, y)
