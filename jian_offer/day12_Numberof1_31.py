# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
# 为此他特别数了一下1~13中包含1的数字有1、10、11、12、13\
# 因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求
# 出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n+1):
            while i :
                if i%10 == 1:
                    count += 1
                i /= 10
        return count

    def NumberOf1Between1AndN_Solution1(self, n):
    	count, m = 0, 1
    	while m <= n:
    		count += (n//m + 8) // 10 * m + (n//m % 10 == 1) * (n%m) + 1
    		m *= 10
    	return count
    	