# -*- encoding:utf-8 -*-
# 查询两个有序数组的中位数

class Solution:
	def medium(self, nums):
		if not nums:
			return False
		med = len(nums) / 2
		return float(nums[med] + nums[med-1]) / 2   if len(nums) %2 == 0 else nums[med]

	def findMedianSortedArrays(self, nums1, nums2):
		newnums = []
		if not nums1:
			newnums = nums2
			return self.medium(newnums)
		if not nums2:
			newnums = nums1
			return self.medium(newnums)
		i, j = 0, 0
		while i < len(nums1) and j < len(nums2):
			if nums1[i] < nums2[j]:
				newnums.append(nums1[i])
			else:
				newnums.append(nums2[j])
		while i < len(nums1):
			newnums.append(nums1[i])
		while j < len(nums2):
			newnums.append(nums2[j])
		return self.medium(newnums)


array1 = [ 1, 4, 7, 8]
array2 = [2, 3, 5, 6, 8, 9]
print(Solution().findMedianSortedArrays(array1, array2))