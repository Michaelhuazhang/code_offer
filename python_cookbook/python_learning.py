# -*- encoding:utf-8 -*-
# a = 1
# def fun(a):
# 	a = 2
# fun(a)
# print(a)

# b = []
# def fun(a):
# 	a.append(1)
# fun(b)
# print(b)

# a = 1
# def fun1(a):
# 	print(id(a))
# 	a = 2
# 	print(id(a), id(2))

# print(id(a), id(1))
# fun1(a)
# print(a)


# class Test(object):  
#     num_of_instance = 0  
#     def __init__(self, name):  
#         self.name = name  
#         Test.num_of_instance += 1  
# # 是可在类的所有实例之间共享的值
# #（也就是说，它们不是单独分配给每个实例的）。
# # 例如下例中，num_of_instance 就是类变量，
# # 用于跟踪存在着多少个Test 的实例。
# if __name__ == '__main__':  
#     print (Test.num_of_instance )  # 0
#     t1 = Test('jack')  
#     print (Test.num_of_instance)   # 1
#     t2 = Test('lucy')  
#     print (t1.name , t1.num_of_instance)  # jack 2
#     print (t2.name , t2.num_of_instance)  # lucy 2

#      # 将列表生成式中[]改成() 之后数据结构是否改变？ 
#      # 答案：是，从列表变为生成器


# 通过列表生成式，可以直接创建一个列表。
# 但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含百万元素的列表，不仅是占用很大的内存空间，
# 如：我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的。
# 因此，没有必要创建完整的列表（节省大量内存空间）。
# 在Python中，我们可以采用生成器：边循环，边计算的机制—>generator

g = (x*x for x in range(10))
l = [x*x for x in range(10)]
print(g, type(g))
print(l, type(l))

# 用*args和**kwargs只是为了方便并没有强制使用它们.

# 当你不确定你的函数里将要传递多少参数时你可以用*args.例如,它可以传递任意数量的参数:

def print_everything(*args):
	for count, thing in enumerate(args):
		print("{0},{1}".format(count, thing))

def table_things(**kwargs):
	for name, value in kwargs.items():
		print("{0}:{1}".format(name, value))

table_things(apple="friit", cabbage="veaetables") 
print_everything("apple", "banban", "orange")