# -*- coding: utf-8 -*-
# @Time    : 2019/01/14 20:27
# @Author  : Michael Zhang
# @Site    : 
# @File    : day4_replaceStr.py
# @Software: Sublime
'''
Q:实现一个函数，将每一个字符串中的每个空格进行替换

A:从后往前替换能够减少移动次数，提高效率
从前往后替换导致覆盖

  如果能够利用空间的话，可以进行新建一个列表进行遍历复制
   


'''

class Solution:
	def replaceSpace(self, s):
		if not isinstance(s, str) or len(s) <= 0 or s == None:
			return ""
		spaceNum = 0
		# 统计空格个数，进行复制
		for i in s:
			if i == " ":
				spaceNum += 1
		newStrLen = len(s) + 2 * spaceNum
		newStr = newStrLen * [None]

		# 设置两个指针
		indexofOrigin, indexofNew = len(s) -1, newStrLen -1

		while indexofOrigin >= 0 and indexofNew >= indexofOrigin:
			if s[indexofOrigin] == " ":
				newStr[indexofNew-2:indexofNew + 1] = ["%", "2", "0"]
				indexofNew -= 3
				indexofOrigin -= 1
			else:
				newStr[indexofNew] = s[indexofOrigin]
				indexofNew -= 1
				indexofOrigin -= 1

		return "".join(newStr)
		