# -*- encoding:utf-8 -*-

dicts = {"ZJH":26, "CLL":27, "js":1,"ah":2}
a = sorted(dicts.items(), key=lambda x: x[1])
print(dicts)
print(a)
array = [2, 4, 1, 3, 8]
array.sort(reverse=True)
print(array)
print(dicts)

d = {key:value for key, value in enumerate(a)}
print(d)


strs = "zhangjianhua "
print(strs[::-1])

str1 = "k:1|k1:2|k2:3|k3:4"

def str2dict(strs):
	dicts = {}
	for item in strs.split("|"):
		key, value = item.split(":")
		dicts[key] = value
	return dicts
print(str2dict(str1))

alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]

print(sorted(alist, key=lambda x:x["age"], reverse=True))

############################################
print("*"*60)
lists = ["a", "b"]
print(lists[10:])# 不报错

#print(lists[10])
# 报错
########
#  列表生成式，生成等差数列为11 的等差数列

print([x*11 for x in range(10)])

print("*"*60)
# 找出两个列表相同的元素或者不同的元素
sets1 = [1, 2, 3]
sets2 = [3, 4, 5]
sets1 = set(sets1)
sets2 = set(sets2)
print(sets1 ^ sets2) # 通过异或操作产生不同的元素
print(sets1 & sets2)# 找出相同的元素

print("*"*60)


# 删除列表当中重复的元素
l1 = ["a", "a", "array", "x", "c", "c"]
l2 = set(l1)
print(l2)

# a. 在python里凡是继承了object的类，都是新式类 

# b. Python3里只有新式类
 # c. Python2里面继承object的是新式类，没有写父类的是经典类 
 # d. 经典类目前在Python里基本没有应用

###########################################3
#4.3 python如何实现单例模式?请写出两种实现方式?

class Solution:
	def reverse(self, x):
		if -10 < x < 10:
			return x
		str_x = str(x)
		if str_x[0] != "-":
			x = int(str_x[::-1])
		else:
			x = -int(str_x[1:][::-1])
		return x if -2147483648<x<2147483647 else 0




print(Solution().reverse(-1234560))

import os
def getfiles(dir, suffix):
	res = []
	for root, dirs, files in os.walk(dir):
		for filename in files:
			name, suf = os.path.splitext(filename)
			if suf == suffix:
				res.append(os.path.join(root, filename))
	print(res)

print(sum(range(0, 101)))


print(0^5)
print("*"*60)
import sys
print(sys.getsizeof(0))
print(sys.getsizeof(456))
print(sys.getsizeof(123456789))
print(sys.maxsize)
print(2**28)
print(2**32)
print(2**64)

print(5&4)
print(5&(~4))
# print(1024**1024)