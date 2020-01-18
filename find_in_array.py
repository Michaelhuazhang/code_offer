# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 11:14 AM
# @Author  : Michael Zhang
# @Site    : 
# @File    : find_in_array.py
# @Software: Sublime


class Solution:
	def Find(self, array, target):
		if array == []:
			return False
		num_row = len(array)
		num_col = len(array[0])
        # 从右上进行查找
		i = num_col - 1  
		j = 0
		while (i >= 0) and (j < num_row):
			if array[j][i] < target:
				j += 1
			elif array[j][i] > target:
				i -= 1
			else:
				return True
				
			