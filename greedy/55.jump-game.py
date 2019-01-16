#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (30.88%)
# Total Accepted:    222.9K
# Total Submissions: 722K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_steps = 0
        for idx, num in enumerate(nums):
            if idx > max_steps:
                return False
            max_steps = max(max_steps, idx+num)
        return True
'''
结果

  ✔ Accepted
  ✔ 75/75 cases passed (72 ms)
  ✔ Your runtime beats 66.75 % of python3 submissions

算法

遍历数组
确定数组中某一位置能不能被走到的条件是

    该位置的下标　小于　之前位置所能提供的最大步数

以　[3,2,1,0,4]　
在位置４时，需要４步，但是之前的位置最多只能提供３步，所以为False

'''
# l = [3,2,1,0,4]
# l = [2,3,1,1,4] 
# l = [3,0,8,2,0,0,1]
# s = Solution()
# print(s.canJump(l))


        
