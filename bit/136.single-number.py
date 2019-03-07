#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (58.75%)
# Total Accepted:    409.9K
# Total Submissions: 697.8K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#
class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':

        r = 0
        for i in nums:
            r ^= i

        return r

        
'''
time O(n) space O(1)
✔ Accepted
✔ 16/16 cases passed (36 ms)
[WARN] Failed to get submission beat ratio.

'''
