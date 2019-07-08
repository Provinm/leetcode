#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (55.51%)
# Likes:    2370
# Dislikes: 200
# Total Accepted:    270.6K
# Total Submissions: 487.5K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return nums

        self._sub(nums, 0, len(nums)-1, 1)
        return nums

    def _sub(self, nums, left, right, temp):
        if left == right:
            _t = nums[left]  
            nums[left] = temp
            return _t
        elif left - right == 1:
            return 1

        sub_temp = temp * nums[left] * nums[right]
        inner_pro = self._sub(nums, left+1, right-1, sub_temp)

        total = inner_pro * nums[left] * nums[right]
        l, r = nums[left], nums[right]
        nums[left] =  inner_pro * r * temp
        nums[right] = inner_pro * l * temp
        return total

# nums = [1,2,3,4, 5]
# s = Solution()
# r = s.productExceptSelf(nums)
# print(r)

'''


Success
Details 
Runtime: 116 ms, faster than 35.86% of Python online submissions for Product of Array Except Self.
Memory Usage: 37.6 MB, less than 5.02% of Python online submissions for Product of Array Except Self.

'''
