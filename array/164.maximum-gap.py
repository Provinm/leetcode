#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap/description/
#
# algorithms
# Hard (32.81%)
# Likes:    522
# Dislikes: 130
# Total Accepted:    71.7K
# Total Submissions: 218.6K
# Testcase Example:  '[3,6,9,1]'
#
# Given an unsorted array, find the maximum difference between the successive
# elements in its sorted form.
# 
# Return 0 if the array contains less than 2 elements.
# 
# Example 1:
# 
# 
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
# (3,6) or (6,9) has the maximum difference 3.
# 
# Example 2:
# 
# 
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
# 
# Note:
# 
# 
# You may assume all elements in the array are non-negative integers and fit in
# the 32-bit signed integer range.
# Try to solve it in linear time/space.
# 
# 
#
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        nums.sort()

        pre, cur = 0, 1
        gap = 0
        while cur < len(nums):

            gap = max(gap, nums[cur]-nums[pre])

            pre += 1
            cur += 1
        
        return gap

