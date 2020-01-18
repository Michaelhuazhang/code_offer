# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:08 PM
# @Author  : Michael Zhang
# @Site    : 
# @File    : minNumberRotate.py
# @Software: Sublime


'''
       把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
       输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。例如数组{3,4,5,1,2}为
       {1， 2， 3， 4， 5}的一个旋转，该数组的最小值为1.Note：给出的所有元素都大于0，若数组
       大小为0，请返回为0

       A：
       二分查找的变形，旋转数组的首元素肯定大于旋转数组的尾元素，找到一个中间点，如果中间点比首元素
       大，说明最小数字在中间点后面，如果中间点比尾元素小，说明最小数字在中间点。然后循环，但是在一次循环中
       ，受元素小于尾元素，说明该数组是有序的。首元素就是最小数字，如果出现首元素、尾元素、中间值三者相等，则只能
       在此区域中顺序查找。



'''
class Solution:
	def minNumberInRotateArray(self, rotateArray):
		# write code here
		if len(rotateArray) == 0:
			return 0
		front = 0
		rear = len(rotateArray) - 1
		minVal = rotateArray[0]

		if rotateArray[front] < rotateArray[rear]:
			return rotateArray[front]
		else:
			while (rear - front) > 1:
				mid = (front + rear) // 2
				if rotateArray[mid] >= rotateArray[front]:
					front = mid
				elif rotateArray[mid] <= rotateArray[rear]:
					rear = mid
				elif rotateArray[front] == rotateArray[rear] == rotateArray[mid]:
					for i in range(1, len(rotateArray)):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                            rear = i
            minVal = rotateArray[rear]
            return minVal


'''
跳台阶

Q: 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''

class Solution:
	def jumpFloor(self, number):
		tempArray = [1, 2]
		if number >= 3:
			for i in range(3, number+1):
				tempArray[(i+1)%2] = tempArray[0] + tempArray[1]
		return tempArray[(number + 1)%2]



'''
变态跳台阶

Q: 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

A: 斐波那契数列的变形
'''
class Solution:
	def jumpFloorII(self, number):
		ans = 1
		if number >= 2:
			for i in range(number - 1):
				ans = ans * 2
		return ans


'''
矩形覆盖

Q: 我们可以用2 1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 1的小矩形无重叠地覆盖一个2 * n的大矩形，总共有多少种方法？

A: 依然是斐波那契数列的变形。代码参考跳台阶。
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        tempArray = [1,2]
        if number >= 3:
            for i in range(3,number+1):
                tempArray[(i+1)%2] = tempArray[0] + tempArray[1]
        return tempArray[(number+1)%2]


'''
二进制中1的个数

Q: 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

A: 每个非零整数n和n-1进行按位与运算，整数n的二进制中，最右边的1就会变成0，利用循环，
计算经过几次运算二进制变成0，就有几个1。
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            count += 1
            n = (n - 1) & n
        return count

print("test")