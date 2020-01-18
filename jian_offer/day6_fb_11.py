# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 23:17
# @Author  : Michael Zhang
# @Site    : 
# @File    : day6_fb_11.py
# @Software: Sublime
# 
'''
斐波那契数列
不使用递归实现数列，把前面的两个数字存入一个数组，实际一直在更新

'''
class Solution:
	def Fibonacci(self, n):
		tempArray = [0, 1]
		if n >= 2:
			for i in  range(2, n):
				tempArray[i%2] = tempArray[0] + tempArray[1]
		return tempArray[n%2]

### 

