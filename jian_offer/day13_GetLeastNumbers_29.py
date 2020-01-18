

'''
输入n个数，找出其中最小的k个数


'''
class Solution:
	# 利用python进行排序
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or  not tinput:
            return []
        tinput.sort()
        return tinput[:k]
    # 利用快排进行排序
    def GetLeastNumbers_Solution1(self, tinput, k):
    	if k > len(tinput) or not tinput:
    		return []
    	tinput = self.quick_sort(tinput)
    	return tinput[:k]

    def quick_sort(self, lst):
    	if not lst:
    		return []
    	pivot = lst[0]
    	left = self.quick_sort([x for x in lst[1:] if x < pivot])
    	right =self.quick_sort([x for x in lst[1:] if x >= pivot])
    	return left + [pivot] + right

    # 时间复杂度为nlogn
    
    