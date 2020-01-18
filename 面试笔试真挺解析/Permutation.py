# -*- encoding:utf-8 -*-


'''
求出一个字符串的全排列
'''
class Solution:
	def Permutation(self, s):
		if not s:
			return []
		if len(s) == 1:
			return list(s)
		charList = list(s)
		charList.sort()
		pStr = []
		for i in range(len(charList)):
			if i > 0 and charList[i] == charList[i-1]:
				continue
			# 如果不允许重复
			temp = self.Permutation("".join(charList[:i]) + "".join(charList[i+1:]))
			for j in temp:
				pStr.append(charList[i] + j)
		return pStr

	def compare(self, s1, s2):
		if not s1 or not s2:
			return False
		if len(s1) != len(s2):
			return False

		res = 0
		s1_list = list(s1)
		s2_list = list(s2)
		for i in s1_list:
			res ^= ord(i)
		for j in s2_list:
			res ^= ord(j)
		if res == 0:
			return True
		else:
			return False

	def isContain(self, s1, s2):
		if not s1 or not s2:
			return False

		len1 = len(s1)
		len2 = len(s2)
		
		if len1 > len2:
			return self.contains12(s1, s2)
		else:
			return self.contains12(s2, s1)

	def contains12(self, s1, s2):
		dict_flag = {}
		for i in s2:
			if i not in dict_flag:
				dict_flag[ord(i)] = 1
			else:
				dict_flag[ord(i)] += 1
		for j in s1:
			if j in dict_flag:
				dict_flag[ord(j)] -= 1
		for value in dict_flag.values():
			if value != 0:
				return False
		return True

# print(Solution().compare("aaaabbc", "abcbaav"))
print(Solution().isContain("acf", "af"))
