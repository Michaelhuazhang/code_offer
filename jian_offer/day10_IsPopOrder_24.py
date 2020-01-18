'''
Q: 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个栈是否是

该栈的弹出顺序

A: 建立一个辅助栈，吧push的数字依次压入栈中，每次压入后，比较辅助栈的栈顶元素和pop序列的首元素
是否相等，相等的话，就退出pop的首元素和辅助栈的栈顶元素，若最后辅助栈
为空，则push的序列对应pop序列

'''

class Solution:
	def IsPopOrder(self, pushV, popV):
		if pushV == [] or popV == []:
			return False
		stack = []
		for i in pushV:# 遍历每一个入栈的结点加入到辅助栈中
			stack.append(i)# 如果辅助栈的栈顶和出栈序列第一个相等，则进行弹出
			while len(stack) and stack[-1] == popV[0]:
				stack.pop() # 弹出最后一个
				popV.pop(0) # 弹出第一个
		if len(stack):# 辅助栈中存在结点，则表明不是
			return False
		else:
			return True
