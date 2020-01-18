# -*- encoding:utf-8 -*-
# import math
# import random
# a = 1
# b = 4
# c = 3
# print(a<b<c)
# print(a < b and b < c)
# print(a/b)
# print(math.e)
# d = random.randint(0, 2)
# print(d)

# # Set 类型是集合内元素位移，元素值不可变的无序集
# seta = set([a, b, c , d])
# print("seta:", seta)
# seta.add("jan")
# seta.update("zhang")
# seta.remove(1)
# print(seta)
# print(seta.intersection("jan"))
# nullset = set()
# print(nullset)
# print({"a", "b"})
# # 注意set只能包含不可变的对象，列表对象，字典对象、set对象不能作为set的元素
# # 元祖可以

# print({1, 2, frozenset({3, 4})})
# # print({1,2, set(1)})

# print({x * x for x in {1, 2, 3, 4}})

array = [1, 5, 2, 4, 8, 6, 9 , 12, 10]
array.sort()
print(array)
# 原地修改
array.sort(reverse=True)
print(array)
array.pop(0)
print(array)
del array[:1]
print(array)
array.insert(0, 123)
print(array)
print(array.index(5))

# sorted(list1,key=None,reverse=False)：排序列表并返回新列表， 非原地修改
# reversed(list1)：返回迭代器，该迭代器迭代结果就是列表的逆序
array2 = [2, 4, 1, 9, 6, 14]
array3 = sorted(array2, reverse=True)
print(array3)

# 如果列表的元素是可变对象的，则对该可变对象的修改会影响到列表。
L = [1,2]
y = [L, 3]
print(y)
L.pop()

print(y)
L = [1, 2, 3]

print(L.append(L))
dic = dict(zip([1,2], ["c", "d"]))
print(dic)
d5 = dict.fromkeys(["a", "b"], 3)
print(d5)
d6 = {"zjh":26, "cll":27}
for i,v in d6.items():
	print(i, v)
v1=v2 = [12, 1230]
v1.append(3)
print(v1)
print(v2)
# X+=Y中，X可以是复杂的对象表达式，只需要求值一次。而X=X+Y中，要对X求值两次
# 对支持原地修改的对象而言，增强形式的赋值会自动执行原地修改的预算
list1 = [3, 4]
oldlist = list1
list1 += [3, 4]
print(oldlist is list1)
print(oldlist)
print(list1)

list2 = [3, 4]
oldlist2 = list2
list2 = list2 + [3, 4]
print(oldlist2 is list2)
print(oldlist2)
print(list2)
# s = input("please input your name:")
# print(s)

# 布尔and和or运算符会返回真或假的操作对象，而不是True或Flase，并且它们是短路计算

# and：从左到右依次对操作对象求值，停在第一个为假的对象上并返回它，或者当前面所有操作对象为真时返回最后一个操作对象
# or：从左到右依次对操作对象求值，停在第一个为真的对象上并返回它，或者当前面所有操作对象为假时返回最后一个操作对象
print(1 and 3)
a = "abcded"
n = [1, 2, 3, 4]
for x,y in zip(a, n):
	print(x,y)
def square(s):
	return s * s

print(map(square, [1, 2, 3]))

import sys
print(sys.maxsize)
