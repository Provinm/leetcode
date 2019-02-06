#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (45.22%)
# Total Accepted:    203.6K
# Total Submissions: 450.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.dfs(root, 0, res)
        return res[::-1]

    def dfs(self, root, deepth, res):

        if len(res) < deepth + 1:
            res.append([])

        res[deepth].append(root.val)
        
        if not root.left and (not root.right):
            return

        if root.left:
            self.dfs(root.left, deepth+1, res)
        
        if root.right:
            self.dfs(root.right, deepth+1, res)

    # def levelOrderBottom(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
        
    #     if root is None:
    #         return []

    #     res = []
    #     stack = [root]
    #     while stack:
    #         new_stack = []
    #         temp_res = []
    #         while stack:
    #             node = stack.pop(0)
    #             temp_res.append(node.val)
    #             if node.left:
    #                 new_stack.append(node.left)
    #             if node.right:
    #                 new_stack.append(node.right)

    #         stack = new_stack
    #         res.append(temp_res)

    #     return res[::-1]

'''
BFS, time O(n) space O(n)

√ Accepted
√ 34/34 cases passed (52 ms)
√ Your runtime beats 24.24 % of python3 submissions


DFS time O(n) space O(n)

√ Accepted
√ 34/34 cases passed (40 ms)
√ Your runtime beats 48.48 % of python3 submissions
'''
