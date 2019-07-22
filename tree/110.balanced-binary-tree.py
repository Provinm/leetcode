#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (41.25%)
# Likes:    1302
# Dislikes: 116
# Total Accepted:    332.1K
# Total Submissions: 805.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        

        def sub(root, height):

            if not root:
                return height, True
            
            left_h, left_is_ok = sub(root.left, height+1)
            right_h, right_is_ok = sub(root.right, height+1)

            r = True
            if abs(left_h-right_h) > 1:
                r = False

            return max(left_h, right_h), r and left_is_ok and right_is_ok

        return sub(root, 0)[1]

'''

Runtime: 36 ms, faster than 93.30% of Python online submissions for Balanced Binary Tree.
Memory Usage: 17.6 MB, less than 5.10% of Python online submissions for Balanced Binary Tree.

'''

