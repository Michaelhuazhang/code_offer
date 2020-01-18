# -*- encoding:utf-8 -*-
# 查找字符串最长回文
# 依次遍历每一个字符，找到最长的回文
# 回文有奇回文和偶回文，abcba是奇回文，abccba是偶回文
# 回文都是中心对称，找到对称点后，同时向前后寻找回文的最长串即可
# 奇回文和偶回文可以归为同一种情况，即abcba以c为对称点，abccba以cc为对称点，
# 但为了代码可读性，可以分开讨论

class Solution:
	def __find_palindrome(self, s, j, k):
		while j >= 0 and k < len(s) and s[j] == s[k]:
			j -= 1
			k += 1
		if self.maxlen < k - j + 1:
			self.maxlen = k - j + 1
			self.retstr = s[j+1:k]

	def longestPalindrome(self, s):
		self.maxlen = 0
		self.retstr = ""
		if len(s) < 2:
			return s
		for i in range(len(s)):
			self.__find_palindrome(s, i, i)
			self.__find_palindrome(s, i, i+1)
		return self.retstr

