# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 23:21
# @Author  : Michael Zhang
# @Site    : 
# @File    : day6_jump_further_12.py
# @Software: Sublime
# 
# 变态跳台阶

# Q: 一只青蛙一次可以跳上1级台阶，
# 也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
	def jumpFloorII(self, number):
		ans = 1
		if number >= 2:
			for i in range(number-1):
				ans *= 2

		return ans