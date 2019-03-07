#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.22%)
# Total Accepted:    182.3K
# Total Submissions: 548.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:

        for row_idx, row in enumerate(obstacleGrid):
            for idx, ele in enumerate(row):
                if ele == 1:
                    obstacleGrid[row_idx][idx] = 0
                elif idx == 0 and row_idx == 0:
                    obstacleGrid[row_idx][idx] = 1  
                elif row_idx == 0:
                    obstacleGrid[row_idx][idx] = obstacleGrid[row_idx][idx-1]
                elif idx == 0:
                    obstacleGrid[row_idx][idx] = obstacleGrid[row_idx-1][idx]
                else:
                    obstacleGrid[row_idx][idx] = obstacleGrid[row_idx-1][idx] + obstacleGrid[row_idx][idx-1]

        return obstacleGrid[-1][-1]

# grid = [[1,0]]
# grid = [[0,0,0],[0,1,0],[0,0,0]]
# s = Solution()
# print(s.uniquePathsWithObstacles(grid))

'''

✔ Accepted
  ✔ 43/43 cases passed (40 ms)
[WARN] Failed to get submission beat ratio.


'''

