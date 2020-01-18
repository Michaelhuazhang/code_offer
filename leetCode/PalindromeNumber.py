# -*- encoding:utf-8 -*-
# 不能使用额外的变量，只能用参数x完成，由于不能使用额外变量的限制，所以代码可读性有点差
# 将int转成str，利用len(str)求出整数的位数，然后用str字符串的切片来取得前后对称部分，如input为x = 1234则len(str(x))为4，3的下标为len(str(x))//2
# 利用python切片可以快速reverse字符串, a = [1,2,3]则a[::-1]为[3,2,1]
# x = 1234可以通过判断12是否等于43来得出是否是回文，根据上一点12可以用切片str(x)[ : len(str(x))//2]求得，43可以根据第4点用str(x)[len(str(x))//2 : ]求得
# 仍然可以分为奇回文和偶回文处理，参考阅读寻找字符串中最长回文，12321以3为对称中心，123321以33为对称中心

class Solution:
	def isPalindrome(self, x):
		if x < 0:
			return False
		if len(str(x)) % 2 == 0:
			return int(str(x)[:len(str(x))// 2]) == int(str(x)[len(str(x)) // 2:][::-1])
		else:
			return int(str(x)[:len(str(x))// 2] ) == int(str(x)[len(str(x))//2 + 1 :][::-1])

print(Solution().isPalindrome(12321))