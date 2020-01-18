# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 20:31
# @Author  : Michael Zhang
# @Site    : 
# @File    : day6_rotateArray_10.py
# @Software: Sublime
# 
'''
旋转数组的最小数字

旋转数组的首元素肯定不小于旋转数组的尾元素
找一个中间点，如果中间点比首元素大，说明最小数字在中间点后面
如果比尾元素小，说明最小数字在中间点前面
但是在一次循环当中，首元素如果小于尾元素，说明该数组是有序的，首元素就是最小数字
如果出现首元素、尾元素、中间值三者相等，则只能在此区域内顺序查找

'''

class Solution:
	def minNumberInrotateArray(self, rotateArray):
		if len(rotateArray) == 0:
			return 0
		front = 0
		rear = len(rotateArray) - 1
		minVal = rotateArray[0]

		if rotateArray[front] < rotateArray[rear]:
			rear rotateArray[front]
		else:
			while (rear - front) > 1:
				mid = (rear + front) // 2
				if rotateArray[front] <= rotateArray[mid]:
					rear = mid
				elif rotateArray[rear] >= rotateArray[mid]:
					front = mid
				elif rotateArray[front] == rotateArray[rear] == rotateArray[mid]:# 只能通过顺序查找
					for i in range(1, len(rotateArray)):
						if rotateArray[i] < minVal:
							minVal = rotateArray[i]
							rear = i
				minVal = rotateArray[rear]
				return minVal
				
