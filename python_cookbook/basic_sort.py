# -*- encoding:utf-8 -*-

# 冒泡排序
class Solution:
	def bubblesort(self, alist):
		for i in range(len(alist)-1, 0, -1):
			for j in range(i):
				if alist[j] > alist[j + 1]:
					alist[j], alist[j+1] = alist[j+1], alist[j]
		return alist


	def bubbleSort(self, alist):
		change = True
		lens= len(alist) - 1
		while lens > 0 and change:
			change = False
			for i in range(lens):
				if alist[i] > alist[i+1]:
					alist[i], alist[i+1] = alist[i+1], alist[i]
					change = True
			lens -= 1
		return alist

	def selectSort(self, alist):
		if not alist or len(alist) == 1:
			return alist
		for i in range(len(alist)-1):
			minindex = i 
			for j in range(i+1, len(alist)):
				if alist[j] < alist[minindex]:
					minindex = j
			alist[i], alist[minindex] = alist[minindex], alist[i]
		return alist




alist = [54,26,93,17,77,31,44,55,20]
print(Solution().bubblesort(alist))
print(Solution().bubblesort([20,30,40,90,50,60,70,80,100,110]))
print(Solution().selectSort(alist))