#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (42.07%)
# Likes:    2762
# Dislikes: 100
# Total Accepted:    379.6K
# Total Submissions: 902.4K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
                return 
            
            grid[i][j] = "0"
            list(map(dfs, (i, i, i+1, i-1), (j+1, j-1, j, j)))

        ret = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == "0":
                    continue
                dfs(i,j)
                ret += 1
                
        return ret


'''

Runtime: 96 ms, faster than 34.05% of Python3 online submissions for Number of Islands.
Memory Usage: 14.2 MB, less than 29.88% of Python3 online submissions for Number of Islands.


''' 
