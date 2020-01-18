# -*- encoding:utf-8 -*-

class Solution:
	def liveDay(self, x, f, d, p):
		p1 = d / x
		if p1 <= f:
			return p1
		rest = d - f * x
		return f + rest / (p + x)

x, f, d, p = map(int, raw_input("").split(" "))
c = Solution().liveDay(x,f, d, p)
print(c)


# 输入包括两行,第一行包括一个整数n(2 ≤ n ≤ 2*10^5),即序列的长度。
# 第二行包括n个整数a_i(1 ≤ a_i ≤ 10^9),即序列a中的每个整数,以空格分割。
n = int(raw_input(""))
a = map(int, raw_input("").split(" "))

# 输入包括字符串s,s的长度length(1 ≤ length ≤ 50),字符串中只包含'0'和'1'
a = raw_input("")

# 输入包括两行,第一行包含整数n(2 ≤ n ≤ 50),即数列的长度。
# 第二行n个元素x[i](0 ≤ x[i] ≤ 1000),即数列中的每个整数。
a = int(raw_input(""))
b = map(int,raw_input("").split(" "))

# 输入包括三行,第一行一个整数n(1 ≤ n ≤ 50),表示棋子的个数
# 第二行为n个棋子的横坐标x[i](1 ≤ x[i] ≤ 10^9)
# 第三行为n个棋子的纵坐标y[i](1 ≤ y[i] ≤ 10^9)
n = int(raw_input(""))
x = map(int,raw_input("").split(" "))
y = map(int,raw_input("").split(" "))
gps = zip(x,y)


