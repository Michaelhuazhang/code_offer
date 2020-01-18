

class solution:
	def InversePairs(self, data):
		return self.inverseCount(data[:], 0, len(data) -1, data[:])%1000000007

	def inverseCount(self, temp, start, end, data):
		if (end - start) < 1:
			return 0
		if end -start == 1:
			if data[start] <= data[end]:
				return 0
			else:
				temp[start], temp[end] = data[end], date[start]
				return 1
		mid = (start + end) // 2
		cnt = self.inverseCount(data, start, mid, temp) + self.inverseCount(data, mid + 1, end, temp)
		i = start
		j = mid +1
		ind = start
		while (i <= mid and j <= end) :
			if data[i] <= data[j]:
				
