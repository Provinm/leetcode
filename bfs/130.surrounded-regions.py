#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (21.81%)
# Total Accepted:    130.1K
# Total Submissions: 596.4K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        # step1 get all O
        x_length = len(board) - 1
        y_length = len(board[0]) - 1

        queue = set()
        boarder = set()

        for i, j_lst in enumerate(board):
            for j, item in enumerate(j_lst):
                if item == "O":
                    # on the boarder
                    if i == 0 or j == 0 or i == x_length or j == y_length:
                        boarder.add((i,j))
                    else:
                        queue.add((i,j))

        # bfs 
        while boarder:
            i, j = boarder.pop()
            directions = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
            for _p in directions:
                if _p in queue:
                    queue.remove(_p)
                    boarder.add(_p)
        
        for i, j in queue:
            board[i][j] = "X"

            
'''
BFS time O(m*n) + worst O(m*n) + worst O(m-2*n-2)

√ Accepted
√ 59/59 cases passed (128 ms)
√ Your runtime beats 41.27 % of python3 submissions
'''


        
