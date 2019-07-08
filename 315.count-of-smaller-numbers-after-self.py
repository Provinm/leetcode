#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (36.65%)
# Total Accepted:    65.7K
# Total Submissions: 179.4K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# Example:
# 
# 
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# 
#

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return []

        counts = [0]
        for idx, item in enumerate(nums[1:], 1):

            for jdx in range(len(counts)):
                tmp = nums[jdx]
                if tmp > item:
                    counts[jdx] += 1

            counts.append(0)

        return counts


# nums = [5]
# s = Solution()
# print(s.countSmaller(nums))

'''

O(n**2) 的算法超时



'''