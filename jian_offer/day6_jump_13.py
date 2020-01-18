# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 20:31
# @Author  : Michael Zhang
# @Site    : 
# @File    : day6_jump_11.py
# @Software: Sublime


class Solution:
	def jumpFloor(self, number):
		tempArray = [1, 2]
		if number >= 3:
			for i in range(number):
				tempArray[(i + 1)%2] = tempArray[0] + tempArray[1]
		return tempArray[(i + 1) % 2]