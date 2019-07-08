#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (55.95%)
# Total Accepted:    99.5K
# Total Submissions: 177.9K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
# 
# Example:
# 
# 
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# 
# Note:
# 
# 
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
# 
#
class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        dct = {}
        for ele in nums:
            if ele in dct:
                del dct[ele]
            else:
                dct[ele] = True
        return list(dct.keys())
