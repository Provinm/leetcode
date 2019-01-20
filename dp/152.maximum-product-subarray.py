#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (28.18%)
# Total Accepted:    180.3K
# Total Submissions: 639.7K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_mins = [(nums[0], nums[0])]
        for idx, ele in enumerate(nums[1:], 1):
            pre = max_mins[idx-1]
            if ele > 0:
                temp = (max(ele, ele*pre[0]), min(ele, ele*pre[1]))
            else:
                temp = (max(ele, ele*pre[1]), min(ele, ele*pre[0]))
            max_mins.append(temp)
        return max(max_mins)[0]


# l = [2,3,-2,4]
# l = [-2,0,-1]
# s = Solution()
# print(s.maxProduct(l))

'''

时间复杂度为 O(N) 空间复杂度为 O(N)

  ✔ Accepted
  ✔ 184/184 cases passed (84 ms)
  ✔ Your runtime beats 23.46 % of python3 submissions

'''
        
