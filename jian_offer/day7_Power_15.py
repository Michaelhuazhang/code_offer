'''
Q: 数值的整数次方

A: 考虑指数是否为负数
底数是否为0，或者接近0


'''

class Solution:
	def power_value(self, base, exponent):
		if exponent == 0:
			return 1
		if exponent == 1:
			return base
		ret = self.power_value(base, exponent >> 1)
		ret *= ret
		# 判断是否为奇数
		if exponent & 1 == 1:
			ret *= base
		return ret

	def Power(self, base, exponent):
		try:
			ret = self.power_value(base, abs(exponent))
			if exponent < 0:
				return 1.0 / ret

		except ZeroDivisionError:
			print("Erro")
		else:
			return ret
			