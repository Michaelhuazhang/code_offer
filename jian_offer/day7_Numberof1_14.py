# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 19:46
# @Author  : Michael Zhang
# @Site    : 
# @File    : day7_numberof1_11.py
# @Software: Sublime
# 

'''
Q: 一个数中有多少个1
通过位运算将n和n-1，消除一个1，有几个1，可以消除几个

用一条语句判断一个整数是不是2 的整数次方
if (n-1)&n == 0


'''
class Solution:
	def NumberOf1(self, number):
		count = 0
		if number < 0:
			number &= 0xffffffff
		while number:
			count += 1
			number &= (number -1)
		return count
	def numchangemn(self, m, n):
		c = m ^ n
		return self.NumberOf1(c)
		

