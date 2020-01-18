# -*- encoding:utf-8 -*-

class Solution:
	def isvalid(self, strs):
		'''
         判断字符串是否符合括号匹配

		'''
		if not strs or len(strs) <= 1:
			return False
		liststrs = list(strs)
		status = 0
		for i in liststrs:
			if i != ")" and i != "(":
				return False
			if i == ")" and (status - 1) < 0:
				return False
			if i == ")":
				status += 1
		return status == 0

	def maxLength(self, strs):
		'''
          以每一个字符结尾最长的有效长度，求出最长的
		'''
		if not strs or len(strs) <= 1:
			return 0
		liststrs = list(strs)
		dp = [0 for i in range(len(strs))]
		pres = 0 
		res = 0
		for i in range(len(liststrs)):
			if liststrs[i] == ")":
				pres = i - dp[i-1] - 1
				# 注意括号匹前面的正确长度也要加上
				if pres >= 0 and liststrs[pres] == "(":
					dp[i] = dp[i-1] + 2 + (dp[pres - 1] if pres > 0 else 0)
			res = max(res, dp[i])
		return res

str1 = "((())())"
print(Solution().isvalid(str1))
print(Solution().maxLength(str1))

str2 = "(())(()(()))"
print(Solution().isvalid(str2))
print(Solution().maxLength(str2))

