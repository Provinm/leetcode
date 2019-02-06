#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (58.74%)
# Total Accepted:    440.6K
# Total Submissions: 750.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        '''dfs
        '''

        if not root:
            return 0

        res = []

        def sub(root, deepth, res):
            if not root.left and not root.right:
                res.append(deepth)

            if root.left:
                sub(root.left, deepth+1, res)

            if root.right:
                sub(root.right, deepth+1, res)

        sub(root, 1, res)
        # print(res)
        return max(res)

    # def maxDepth(self, root: 'TreeNode') -> 'int':

    #     if not root:
    #         return 0

    #     stack = [root]
    #     deepth = 0
    #     while stack:

    #         # node = stack.pop(0)
    #         new_stack = []
    #         while stack:
    #             node = stack.pop()
    #             if node.left:
    #                 new_stack.append(node.left)

    #             if node.right:
    #                 new_stack.append(node.right)

    #         deepth += 1
    #         stack = new_stack


    #     return deepth


'''
BFS time O(N) space O(N)
✔ Accepted
✔ 39/39 cases passed (44 ms)
[WARN] Failed to get submission beat ratio.


DFS time O(n) space O(k) 

✔ Accepted
✔ 39/39 cases passed (44 ms)
[WARN] Failed to get submission beat ratio.


'''


        
