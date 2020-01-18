
# -*- encoding:utf-8 -*-

class Solution:
	def RightRotateString(self, strs, m):
		if not strs:
			return
		str_list = list(strs)
		length = len(strs)
		m = m % length
		str_list = self.Reverse(str_list, 0, length - 1)
		str_list = self.Reverse(str_list, 0, m-1)
		str_list = self.Reverse(str_list, m, length -1)
		return str_list



	def Reverse(self, strs, start, end):
		if not strs:
			return
		while start < end:
			strs[start], strs[end] = strs[end], strs[start]
			start += 1
			end -= 1
		return strs

	def StringContain(self, s1, s2):
		if not s1 or not s2:
			return False
		list_1 = list(s1)
		list_2 = list(s2)
		hash_s = 0

		for i in list_1:
			hash_s |= 1 << (ord(i) - ord("A"))
		for j in list_2:
			if (hash_s & (1 << (ord(j) - ord("A"))) == 0):
				return False

		return True

	def StringContains(self, s1, s2):
		if not s1 or not s2:
			return False
		dict_s = {}
		list_1 = list(s1)
		list_2 = list(s2)
		for i in list_1:
			if i not in dict_s:
				dict_s[i] = 1
		for j in list_2:
			if j not in dict_s:
				return False
		return True


	def Permutation(self, strs):
		if not strs:
			return None
		if len(strs) == 1:
			return [list(strs)]
		list_s = list(strs)
		list_s.sort()
		res = []
		for i in range(0, len(list_s)):
			if i > 0 and list_s[i-1] == list_s[i]:
				continue
			temp = self.Permutation("".join(list_s[:i]) + "".join(list_s[i + 1:]))
			for j in temp:
				res.append([list_s[i]] + j)
		return res



print(Solution().RightRotateString("abcdef", 3))

print(Solution().StringContain("abaddd", "abd"))
print(Solution().Permutation("abddc"))