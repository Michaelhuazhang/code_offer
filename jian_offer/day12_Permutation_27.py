#  输入一个字符串,按字典序打印出该字符串中字符的所有排列。
#  例如输入字符串abc,
#  则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
#  
#  

#  
#Answer :
# 固定一个元素，求出后面所有字符的排列，重新固定第一个元素，再求出后面的排列
#     

class Solution:
	def Permutation(self, ss):
		if not ss:
			return []
		if len(ss) == 1:
			return list(ss)

		charList = list(ss)
		charList.sort()
		pStr = []
		for i in range(0, len(charList)):
			if i > 0 and charList[i] == charList[i-1]:
				continue
			temp = self.Permutation("".join(charList[:i]) + ''.join(charList[i+1:]))
			for j in temp:
				pStr.append(charList[i] +j)
		return pStr
		
