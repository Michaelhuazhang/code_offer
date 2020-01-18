# -*- encoding:utf-8 -*-

'''
A、B玩家，从左右各拿一个轮流拿，最后谁赢，返回分数


'''
class Soludtion:
	# 一个数组（i, j）,作为先发者能够获得最好的分数
	def firstscore(self, array, i, j):
		if i == j:
			return array[i]
		return max(array[i] + self.nextscore(array, i+1, j), array[j] + self.nextscore(array, i, j-1))

	def nextscore(self, array, i, j):
		# 作为后发者，能够获得最好的分数
		if i == j:
			return 0
		return min(self.firstscore(array, i + 1, j), self.firstscore(array, i, j - 1))# 只能得到最差的

	def whowin(self, array):
		if not array or len(array) <= 0:
			return 0
		sum_array = sum(array)
		f1 = self.firstscore(array, 0, len(array) - 1)
		f2 = sum_array - f1
		return max(f1, f2)

	def whowin2(self, array):
		if not array or len(array) <= 0:
			return 0
		first = [[0 for i in range(len(array))] for i in range(len(array))]
		second = [[0 for i in range(len(array))] for i in range(len(array))]
		j = 0
		i = 0
		while j < len(array):
			first[j][j] == array[j]
			i = j - 1
			while i >=0:
				first[i][j] = max(array[i] + second[i+1][j], array[j] + second[i][j-1])
				second[i][j] = min(first[i+1][j], first[i][j-1])
				i -= 1

			j += 1
		return max(first[0][len(array)-1], second[0][len(array) - 1])

	def firstscore_wan(self, array, i, j):
		if i == j:
			return array[i]
		if i + 1 == j:
			return max(array[i], array[j])
		return max(
                 array[i] + min(self.firstscore_wan(array, i + 2, j), self.firstscore_wan(array, i+1, j-1)),
                 array[j] + min(self.firstscore_wan(array,i + 1 ,j - 1), self.firstscore_wan(array, i, j - 2))
			)

# print(Soludtion().whowin([1,4, 5, 6,1]))
# print(Soludtion().whowin2([1,4, 5, 6,1]))
# 递归存在大量重复，无后效性可以这样改



# 题目1
# 已知一个字符串都是有左右括号组成的，判断该字符串是否是有效的括号组合

# A: 遇到左括号++，右括号--，如果减到负，false，最后如果为0

# 进阶：
# 已知一个字符串都是有左右括号组成的，返回有效的长度

#（（）（）（）（）（
# 求必须以某个字符结尾的有效字串长度，返回最长



class Solution1:
	def isValid(self, strs):
		if not strs or len(strs) <= 0:
			return False
		charlist = list(strs)
		staus = 0
		for i in charlist:
			if i != "(" and i != ")":
				return False
			if i == ")":
				staus -= 1
				if staus < 0:
					return False
			if i == "(":
				staus += 1
		if staus != 0:
			return False
		else:
			return True


	def maxlength(self, strs):
		if not strs or len(strs) <= 0:
			return 0
		charlist = list(strs)
		dp = [0 for i in range(len(strs))]
		pre = 0
		res = 0
		i = 0
		while i < len(strs):
			if charlist[i] == ")":
				pre = i - dp[i - 1] - 1
				if pre >= 0 and charlist[pre] == "(":
					dp[i] = dp[i - 1] + 2  + (dp[pre-1] if pre > 0 else 0)
			res = max(res, dp[i])
			i += 1
		return res

print(Solution1().isValid("((()))）"))
print(Solution1().maxlength("((()))()(())"))

### 题目二：
字串和子数组以开头或者结尾
# 给定一个数组，值全为正数，请返回累加和为定值的最长子数组长度
    1、左右两个指针，右指针滑动，记录等于k的长度
    当长度大于K，作指针右滑，继续（都是正数，所以这个数不在可能，右滑动）
    总结就是统计每个数开始的最长长度的最长子数组
 

# 给定一个数组，值可正可负和0，返回累加和为定值k的最长子数组长度
      以每个数组中每个数结尾的最长

# 给定一个数组，值可正可负和0，返回累加和小于等于定值k的最长子数组长度


class Solution2:
	def 
