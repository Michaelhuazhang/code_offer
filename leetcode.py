# -*- encoding:utf-8 -*-
import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def two_sum(arr, target):
	if not arr or len(arr) < 2:
		return [-1, -1]
	maps = {}
	for i in range(len(arr)):
		if target - arr[i] in maps:
			return [maps[target - i], i]

		maps[arr[i]] = i
	return [-1, -1]

def two_sumNode(head1, head2):
	if not head1 and not head2:
		return None
	if not head2 or not head1:
		return head1 or head2
	dummy = Node(0)
	p1 = head1
	p2 = head2
	temp = 0
	cur = dummy
	while p1 or p2:
		if p1:
			temp += p1.val
			p1 = p1.next
		if p2:
			temp += p2.val
			p2 = p2.next
		cur.next = Node(temp % 10)
		cur = dummy.next
		temp //= 10
	if temp == 1:
		cur.next = Node(1)
	return dummy.next



def lengthLongestSubString(strs):
	'''
     记录起点位置
	'''
	if not strs or len(strs) == 0:
		return 0
	maps = {}
	res = 0
	j = 0
	for i in range(len(strs)):
		if strs[i] in maps:
			j = max(j, maps[strs[i]] + 1)
		maps[strs[i]] = i
		res = max(res, i - j + 1)
	return res


def medianTwoSortedArray(arr1, arr2):
	'''
     两个有序数组寻找中位数
     了解arr1如何切，就可以知道arr2切
     cut1,cut2分别代表左侧有几个数字
     cut1两侧l1，r1
     cut2两侧l2，r2
     l1<=R2
     l2 <=R1
     如果l1>r2  cut1向左侧移动
     如果l2>r1  cut1向右侧移动

	'''

	if not arr1 or not arr2:
		return None
	if not arr1:
		return (arr2[len(arr2) // 2] + arr2[len(arr2) // 2 - 1]) / 2 if len(arr2) % 2 == 0 else arr2[len(arr2) // 2]
	if not arr2:
		return (arr1[len(arr1) // 2] + arr1[len(arr1) // 2 - 1]) / 2 if len(arr1) % 2 == 0 else arr1[len(arr1) // 2]

	if len(arr2) < len(arr1):
		return medianTwoSortedArray(arr2, arr1)
	lens = (len(arr1) + len(arr2))
	cut1 = 0
	cut2 = 0

	# cut1 在cutL 和cutR中切
	cutL = 0
	cutR = len(arr1) - 1
	while cut1 <= len(arr1):
		cut1 = cutL + ((cutR - cutL) >> 1)
		cut2 = (lens //2) - cut1
		l1 = -sys.maxsize if cut1 == 0 else arr1[cut1 - 1]
        R1 = sys.maxsize if cut1 == len(arr1) else arr1[cut1]
        l2 = -sys.maxsize if cut2 == 0 else arr2[cut2 - 1]
        R2 = sys.maxsize if cut2 == len(arr2) else arr2[cut2]

        if l1 > R2:
        	cutR = cut1 - 1
        elif l2 > r1:
        	cutL = cut1 + 1
        else:
        	if lens % 2 == 0:
                l1 = l1 if l1 > l2 else l2
                R1 = R1 if R1 < R2 else R2
                return (l1 + R1) / 2
            else:
                R1 = R1 if R1 < R2 else R2
                return R1
    return -1



class Solution1:
    def __init__(self):
        self.res = ""




    def longestPalindrome(self, s):
        '''
        中心扩散
        :param s:
        :return:
        '''

        if not s or len(s) == 0:
            return s
        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i+1)
        return self.res

    def helper(self, s, left, right):
        while (left >= 0) and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if right - left - 1 > len(self.res):
            self.res = s[left+1:right]



def reverseInteger(num):
	res = 0
	flag = 1
	if num < 0:
		flag = - 1
		num = -num
	while num != 0:
		res = res * 10 + num % 10
		if res > 2 ** 31 - 1 or res < - 2 ** 32:
			return 0
		num //= 10
	return res * flag


def str2Integer(strs):
	if not strs or len(strs) == 0:
		return 0
	s = strs.strip()
	sign = 1
	start = 0
	res = 0
	if s[0] == "-":
		sign = -1
		start = 1
	if s[0] == "+":
		sign = 1
		start = 1
	for i in range(start, len(s)):
		if not s[i].isdigit():
			return sign * res
		res = 10 * res + ord(s[i]) - ord('0')
		if res > 2 ** 31 - 1 or res < -2 ** 32:
			return 0
	return res * sign

def isPalindrome(x):
	if x < 0 or (x != 0 and x % 10 == 0):
		return False
	palind = x
	res = 0
	while x != 0:
		res = res * 10 + x % 10
		x //= 10
	return res == palind

def containsMostWater(height):
	res = 0
	l = 0
	r = len(height) - 1
	while l <= r:
		res = max(res, min(height[l], height[r]) * (r - l))
		if height[l] < height[r]:
			l += 1
		else:
			r -= 1
	return res


def int2Roman(num):
	values = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX",
                  5: "V", 4: "IV", 1: "I"}
    res = []
    for i in values.keys():
    	while num >= i:
    		num -= i
    		res.append(values[i])
    return "".join(res)

    def toNumber(c):
        res = 0
        if c == "I":
            return 1
        elif c == "V":
            return 5
        elif c == "X":
            return 10
        elif c == "L":
            return 50
        elif c == "C":
            return 100
        elif c == "D":
            return 500
        elif c == "M":
            return 1000
        else:
            return res
def romantoInteger(s):
	'''
    左边的数字小于右边， 右边 - 左边
    res + 左边 - 右边 * 2
	'''
	if not s or len(s) == 0:
		return 0
	res = toNumber(s[0])
	for i in range(1, len(s)):
		if toNumber(s[i]) > toNumber(s[i-1]):
			res += toNumber(s[i]) - 2 * toNumber(s[i-1])
		else:
			res += toNumber(s[i])
	return res


def longestCommonPrefix(strs):
	if not strs or len(strs) == 0:
		return 0
	res = strs[0]
	for i in range(1, len(strs)):
		while strs[i].find(res) != 0:
			res = res[:len(res) - 1]
	return res


def threeSum(arr):
	if not arr or len(arr) == 0:
		return -1
	arr.sort()
	res = []
	for i in range(len(arr) - 2):
		if i > 0 and arr[i] == arr[i-1]:
			continue
		low = i + 1
		high = len(arr) - 1
		temp_sum = - arr[i]
		while low < high:
			if arr[low] + arr[high] == temp_sum:
				res.append[arr[i], arr[low], arr[high]]
				while low < high and arr[low] == arr[low + 1]:
					low += 1
				while low < high and arr[high] == arr[high-1]:
					high -= 1
				low += 1
				high -= 1
			elif arr[low] + arr[high] > temp_sum:
				high -= 1
			else:
				low += 1
	return res

def threeSumCloested(arr, target):
	if not arr or len(arr) < 3:
		return 0 

	res = arr[0] + arr[1] + arr[len(arr) - 1]
	res.sort()
	for i in range(len(arr)-2):
		start = i + 1
		end = len(arr) - 1
		while start < end:
			sums = arr[i] + arr[start] + arr[end]
			if sums > target:
				end -= 1
			else:
				start += 1
			if abs(sums - target) < res:
				res = sums
	return res

def fourSum(arr):
	res = []
	if not arr or len(arr) < 4:
		return 0
	arr.sort()
	for i in range(len(arr) - 3):
		if i > 0 and arr[i] == arr[i-1]:
			continue
		for j in range(i+1, len(arr) - 2):
			if j > i+1 and arr[j] == arr[j-1]:
				continue
			start = j + 1
			end = len(arr) - 1
			while start < end:
				temp_sum = target - arr[i] - arr[j] - arr[start] - arr[end]
                if temp_sum == 0:
                    res.append([arr[i], arr[j], arr[start], arr[end]])
                    # 去重
                    while start < end and arr[start] == arr[start + 1]:
                        start += 1
                    while start < end and arr[end] == arr[end -  1]:
                        end -= 1
                    # 更新
                    start += 1
                    end -= 1
                elif temp_sum > 0:
                    end -= 1
                else:
                    start += 1
    return res

def removeNthNodeFromEndToFirst(head, n):
	dummy = Node(0)
	slow = dummy
	fast = dummy
	dummy.next = head
	for i in range(n+1):
		fast = fast.next
	while fast:
		fast = fast.next
		slow = slow.next
	slow.next = slow.next.next
	return dummy.next

def validParenthess(s):
	if not s or len(s) == 0:
		return True
	stack = []
	for i in s:
		if i == "(":
			stack.append(")")
		elif i == "{":
			stack.append("}")
		elif i == "[":
			stack.append("]")
		else:
			if len(stack) == 0 or stack.pop() != i:
				return False
	return len(stack) == 0

def mergeTwoSortedList(self, head1, head2):
    dummy = Node(0)
    p1 = head1
    p2 = head2
    cur = dummy
    while p1 and p2:
        if p1.val < p2.val:
            cur.next = p1
            p1 = p1.next
        else:
            cur.next = p2
            p2 = p2.next
        cur = cur.next
    if p1:
        cur.next = p1
    if p2:
        cur.next = p2
    return dummy.next

def mergeTwoSortedLis(self, head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.val < head2.val:
        head1.next = self.mergeTwoSortedLis(head1.next, head2)
        return head1
    else:
        head2.next = self.mergeTwoSortedLis(head1, head2.next)
        return head2

print("aaa")
print(Solution1().longestPalindrome("abba"))

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.singleStr('', 0, 0, n)
        return self.res
        
    def singleStr(self, s, left, right, n):
    	'''
    	先加左括号后加右括号，保持始终能够配对
    	选择：加左括号，加右括号
    	结束：左括号用完，右括号也用完，不能在家
    	一定是正确解，保持加入的顺序
    	'''
        if left == n and right == n:
            self.res.append(s)
        if left < n:
            self.singleStr(s + '(',left + 1, right, n)
        if right < left:
            self.singleStr(s + ')',left, right + 1, n)


def mergeSortedKists(self, lists):
    if not lists or len(lists) == 0:
        return None
    return self.resort(lists, 0, len(lists) - 1)

def resort(self, lists, low, high):
    if low >= high:
        return lists[low]
    mid = low + ((high - low) >> 1)
    l1 = self.resort(lists, low, mid)
    l2 = self.resort(lists, mid+1, high)
    return self.merge(l1, l2)

def merge(self, l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        l1.next = self.merge(l1.next, l2)
        return l1
    if l2.val < l1.val:
        l2.next = self.merge(l1, l2.next)
        return l2
class TreeNode:
	def __init__(self, data):
        self.data = data
          
        self.lchild = None
        self.rchild = None
        self.parent = None
def priorityMergeKLists(self, lists):
    import heapq
    if not lists or len(lists) == 0:
        return None
    heapq.heapify(lists)
    dummy = Node(0)
    cur = dummy
    while len(lists) != 0:
        cur.next = heapq.heappop(lists)
        cur = cur.next
        if cur.next:
            heapq.heappush(cur.next)
    return dummy.next

