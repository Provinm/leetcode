#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (26.89%)
# Total Accepted:    146.2K
# Total Submissions: 543.8K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)-1
        ptr = 0
        step = 0
        while ptr < length:
            num = nums[ptr]
            if num + ptr >= length:
                step += 1
                break
            max_step = 0
            max_idx = -1
            count = num
            while count > 0:
                idx = ptr + count
                if max_step < nums[idx]+count:
                    max_step = nums[idx]+count
                    max_idx = count 
                count -= 1

            step += 1
            ptr += max_idx
        
        return step


# l = [2,3,1,1,4]
# l = [5,5,5,5]
# l = [1,1,1,1]
# s = Solution()
# print(s.jump(l))    
'''

结果

✔ Accepted
✔ 92/92 cases passed (80 ms)
✔ Your runtime beats 71.43 % of python3 submissions

算法分析

使用贪心算法，每一次尽量走最多的步数

[2,3,1,1,4]

当计算到 2 时,能走的步数为 1　或者　２
然后计算走 1　或者 2 时接着走的最大步数
可以得到

2-1+3 > 2+1 

所以第一次走 1 步即可

如此循环

'''
