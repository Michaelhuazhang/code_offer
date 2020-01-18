# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 16:11
# @Author  : Michael Zhang
# @Site    : 
# @File    : reorderArray.py
# @Software: Sublime

'''
Q: 输入一个整数数组，实现一个函数来调整数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变

'''

class Solution:
	def reorderArray(self, array):
		return sorted(array, key=lambda x:x%2, reverse=True)

print(Solution().reorderArray([1,2,3,4]))
