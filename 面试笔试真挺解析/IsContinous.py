# -*- encoding:utf-8 -*-


# LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
# 他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
# “红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,
# 并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。

# LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，
#否则就输出false。
# 为了方便起见,你可以认为大小王是0。

'''
A: 将5张牌组成的顺子看成数组
 对数组进行排序
 求出大小王的个数即0的个数
 求出数组中的数字间隔
 比较间隔和0的个数
 若出现成对的，则一定不是顺子
'''

class Solution:
	def Iscontinous(self, numbers):
		if not numbers or len(numbers) == 0:
			return False
		transdict = {"A":1, "J":11, "Q":12, "K":13}
		for i in range(len(numbers)):
			if i in transdict.keys():
				i = transdict[i]
		numbers = sorted(numbers)
		number_0 = 0
		number_gap = 0
		for i in numbers:
			if i == 0:
				numbers += 1
		front = number_0
		behind = front + 1
		while behind < len(numbers):
			if numbers[front] == numbers[behind]:
				return False
			number_gap += numbers[behind] - numbers[front] - 1
			front = behind
			behind += 1
		return False if number_gap > number_0 else True

	def LastRemaining_Solution(self, n, m):
		'''
	
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,
自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)


A: 约瑟夫环的问题
  幸存者满足Pn = (pn-1 + k)%n

		'''
		if n < 1 or m < 1:
			return -1
		idx = 0
		for i in range(1, n+1):
			idx = (idx + m) % i
		return idx
		




