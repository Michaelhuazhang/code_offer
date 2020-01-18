# -*- coding: utf-8 -*-
# @Time    : 2019/01/14 20:18
# @Author  : Michael Zhang
# @Site    : 
# @File    : day4_findinArray.py
# @Software: Sublime
'''
Q:P44  二维数组中的查找

A:从左下和右上开始查找，每次查找要缩小查找范围
'''
class Solution:
	def Find(self, target, array):
		if array == []:
			return False
		num_row = len(array)
		num_col = len(array[0])
		# From the right up
		i = 0
		j = num_col -1 

		while i < num_row and j >= 0:
			if array[i][j] > target:
				j -= 1
			if array[i][j] < target:
				i += 1
			if array[i][j] == target:
				return True
		return False
		