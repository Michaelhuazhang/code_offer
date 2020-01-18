# -*- encoding:utf-8 -*-
# 求解最长不重复字串
# 思路(时间复杂度为O(n))

# 遍历字符串，过程中将出现过的字符存入字典，key为字符，value为字符下标
# 用maxLength保存遍历过程中找到的最大不重复子串的长度
# 用start保存最长子串的开始下标
# 如果字符已经出现在字典中，更新start的值
# 如果字符不在字典中，更新maxLength的值
# return maxLength
class Solution:
	def lengthOfLongestSubString(self, s):
		start = maxLength = 0
		usedChar = {}
		for i in range(len(s)):
			if s[i] in usedChar and start <= usedChar[s[i]]:
				start = usedChar[s[i]] + 1
			else:
				maxLength = max(maxLength, i - start + 1)
			usedChar[s[i]] = i
		return maxLength


		