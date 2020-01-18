# -*- encoding:utf-8 -*-
'''
KMP:问题


'''

class Solution:
	def getNextArray(self, str2):
		if not str2:
			return None
		if len(str2) == 1:
			return [-1]
		next_str = [1] * len(str2)
		next_str[0] = -1
		next_str[1] = 0
		i = 2
		cn = 0# 跳到的位置（最长前缀）
		while i < len(next_str):
			if str2[i-1] == str2[cn]:
				next_str[i] = cn + 1
			elif cn > 0:
				cn = next_str[cn] # 往前跳(next数组前的位置)
			else:
				next_str[i] = 0
			i += 1
		return next_str

	def getIndexOf(self, str1, str2):
		if not str1 or not str2 or len(str1) < 1 or len(str1) < len(str2):
			return -1
		list_str1 = list(str1)
		list_str2 = list(str2)
		i1 = 0
		i2 = 0
		next_str = self.getNextArray(list_str2)

		while i1 < len(str1) and i2 <len(str2):
			if list_str1[i1] == list_str2[i2]:
				i1 += 1
				i2 += 1	#往后滑动
			elif next_str[i2] == -1:
				i1 += 1 # 说明配不成功，主串+1，字串重新开始
			else:
				i2 = next_str[i2] # 字串从最长前缀开始匹配

		return i1 -i2 if i2 == len(str2) else -1

print(Solution().getIndexOf("abdfefgabdfc", "gabd"))
