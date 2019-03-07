#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (44.99%)
# Total Accepted:    156.6K
# Total Submissions: 348.1K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,3,2]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [0,1,0,1,0,1,99]
# Output: 99
# 
#
class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        
        a = b = 0
        for i in nums:

            a = a ^ i & ~b
            b = b ^ i & ~a
            # print(a, b)

        return a|b

# nums = [10,1,10,1,10,1,99]
# s = Solution()
# print(s.singleNumber(nums))

'''
✔ Accepted
  ✔ 11/11 cases passed (40 ms)
[WARN] Failed to get submission beat ratio.
'''
