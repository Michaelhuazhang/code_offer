'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，
就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！


A: 
(1) 逆置前K，逆置后，逆置所有
 逆置头和尾不断交换

'''
def Solution:
	def LeftRotateString(self, s, n):
		if not s or len(s) < n or len(s) <= 0 or n < 0:
			return ''
		if len(s) == n:
			return s
		lis = list(s)
		left = self.Reverse(lis[:n])
		right = self.Reverse(lis[n:])
		res = self.Reverse(left + right)
		return "".join(res)


	def Reverse(self, lis):
		if not lis or len(lis) <= 0:
			return []
		start = 0
		end = len(lis) - 1 
		while start < end:
			lis[start], lis[end] = lis[end], lis[start]
			start += 1
			end -= 1
		return lis