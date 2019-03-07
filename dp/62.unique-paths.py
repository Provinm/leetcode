#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (46.26%)
# Total Accepted:    257.9K
# Total Submissions: 557.4K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        res = [[0 for i in range(m)] for j in range(n)]

        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    res[j][i] = 1
                     
                else:
                    res[j][i] = res[j-1][i] + res[j][i-1]

        return res[-1][-1]

# m = 3
# n = 2
# s = Solution()
# print(s.uniquePaths(m,n))

'''
✔ Accepted
  ✔ 62/62 cases passed (40 ms)
[WARN] Failed to get submission beat ratio.
'''


        
