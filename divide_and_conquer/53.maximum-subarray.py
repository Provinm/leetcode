#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (42.35%)
# Total Accepted:    437.3K
# Total Submissions: 1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cur_s = max_s = nums[0]

        for item in nums[1:]:

            cur_s = max(item, item+cur_s)
            max_s = max(cur_s, max_s)

        return max_s

'''
这个答案我想不出来，是抄的 leetcode discussion 
太牛逼了

  ✔ Accepted
  ✔ 202/202 cases passed (68 ms)
  ✔ Your runtime beats 80.32 % of python3 submissions

'''
