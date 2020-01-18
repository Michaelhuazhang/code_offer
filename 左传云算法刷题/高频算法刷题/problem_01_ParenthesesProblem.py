# -*- encoding:utf-8 -*-

# Q: 字符串只有括号，判断是否为正确匹配
# Q：判断一个字符串最长括号匹配的长度

class Solution:
	def isValid(self, strs):
		if not strs or len(strs) <= 1:
			return 0
		status = 0 # 记录左括号
		# 遍历字符串，遇到左括号，++，右括号--，当为负的时候判断否
		for i in strs:
			if i != "(" and i != ")":
				return False
			if i == "(":
				status += 1
			if i == ")":
				status -= 1
				if status < 0:
					return False
		return status == 0

	def maxlength(self, strs):
		if not strs or len(strs) <= 1:
			return 0
		# 记录以每个字符结尾的有效匹配，返回最大
		dp = [0 for i in strs]
		pre = 0
		res = 0 
		for i in range(1, len(strs)):
			if strs[i] == ")":
				pre = i - dp[i-1] - 1
				if pre >= 0 and strs[pre] == "(":
					dp[i] = dp[i-1] + 2 + (dp[pre-1] if pre > 0 else 0) # 注意要加上先前的匹配
			res = max(res, dp[i])
		return res

print(Solution().isValid("((((()))"))
print(Solution().isValid("()()(())"))
print(Solution().maxlength("()()(())"))