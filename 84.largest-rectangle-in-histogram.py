#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (29.77%)
# Total Accepted:    151.8K
# Total Submissions: 509.5K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        if not heights:
            return 0

        max_ptr, min_ptr = (heights[0], 0), (heights[0], 0)
        max_res = heights[0]

        for idx, item in enumerate(heights[1:], 1):

            temp_area = item
            if item >= max_ptr[0]:
                max_ptr = (item, idx)

            elif item <= min_ptr[0]:
                min_ptr = (item, idx)

            # 计算 min_ptr 和 max_ptr 中的最大面基

            diff = abs(max_ptr[1] - min_ptr[1])
            while diff > 0:
                diff -= 1


            # forward = diff // abs(diff)

            # for _idx in range(min_ptr, max_ptr, forward):



