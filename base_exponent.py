# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 15:58 
# @Author  : Michael Zhang
# @Site    : 
# @File    : base_exponent.py
# @Software: Sublime
'''
Q: 给定一个double类型的浮点数base和int类型的整数exponent，求base的exponent

A: 如果用常规的算法，要注意：指数为负数的时候；底数为0且指数为负数的时候
这种情况可以直接通过底数==0来判断，计算机内表示有小数有误差，只能判断他们的差的绝对值是不是在一个很小的范围N内
所以用递归好一点，利用右移一位实现除以2运算，用&1运算，判断是否为奇数，能够提高效率
'''

class Solution:
	def Power(self, base, exponent):
		try:
			ret = self.power_value(base, abs(exponent))
			if exponent < 0:
				return 1.0 / ret
		except ZeroDivisionError:
			print("Error : base is zero")
		except:
			return ret

	def power_value(self, base, exponent):
		if exponent == 0:
			return 1
		if exponent == 1:
			return base
		ret = self.power_value(base, exponent >> 1)
		ret *= ret
		if except & 1 == 1:
			ret *= base
		return ret
		