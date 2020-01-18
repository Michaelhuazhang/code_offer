
'''
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？


A: 首先将输入的字符串完全反转，从前往后遍历新字符串，遇到空格，就将空格前的字符串翻转，添加空格，继续遍历
遍历到结尾的时候，因为最后一个字符串后没有空格，所以要最后再翻转

'''

class Solution:
	def ReverseSentence(self, s):
		if not a or len(s) <= 0:
			return ""
		lis = list(s)
		lis = self.Reverse(lis)
		start = 0
		end = 0
		res = ""
		listemp = []
		while end < len(s):
			if end == len(s) - 1:
				listemp.append(self.Reverse(lis[start:]))
				break
			if lis[start] == " ":
				start += 1
				end += 1
				listemp.append(" ")
			elif lis[end] == " ":
				listemp.append(self.Reverse(lis[start:end]))
				start = end

			else:
				end += 1
		return "".join(listemp)
		


	def Reverse(self, lis):
		if not lis or len(lis) <= 0:
			return []
		start = 0
		end = len(start) - 1
		while start < end:
			lis[start], lis[end] = lis[end], lis[start]
			start += 1
			end -= 1
		return lis