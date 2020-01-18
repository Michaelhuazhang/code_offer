

class Solution:
	def findone(self, array):
		if array == None:
			return
		result = 0
		for i in array:
			result ^= i
		return result

	def findTwo(self, array):
		result = 0
		result = self.findone(array)
		temp = result
		tempresult = result
		position = 0
		while temp & 1 == 0:
			position += 1
			temp = temp >> 1

		for i in array:
			if ((i >> position) & 1) == 1:
				result = result ^ i
		return result, result ^ tempresult
# print(Solution().findone([3, 5, 6, 6, 5,  2, 2]))
print(Solution().findTwo([3, 5, 6, 6, 5, 7, 2, 2]))