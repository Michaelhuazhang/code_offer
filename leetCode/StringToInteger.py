# -*- encoding:utf-8 -*-
# 思路

# 利用Python内置的int(str)函数可以将字符串快速转换成int型
# 利用int(str)是否抛出异常来快速判断str能否被转换成int，进而迅速确定输入字符串中第一个非数字字符的位置
# 需要注意处理+,-符号的问题


class Solution:
	def myAtoi(self, s):
		s = s.strip()
		retstr = ""
		try:
			for _, item in enumerate(s):
				if item == "+" or item == "-":
					retstr += item
				else:
					retstr += str(int(item))
		finally:
			if len(retstr) == 0:
				retstr 0
			else:
				try:
					return int(retstr)
				except:
					return 0
					