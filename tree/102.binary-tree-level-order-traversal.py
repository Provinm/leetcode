#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (47.10%)
# Total Accepted:    339.3K
# Total Submissions: 720.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
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
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            new_stack = []
            temp = []
            while stack:
                node = stack.pop(0)
                temp.append(node.val)

                if node.left:
                    new_stack.append(node.left)

                if node.right:
                    new_stack.append(node.right)

            stack = new_stack
            res.append(temp)

        return res


'''

BFS time 0(n) space O(n)
✔ Accepted
  ✔ 34/34 cases passed (44 ms)
  ✔ Your runtime beats 55.46 % of python3 submissions
  ✔ Your memory usage beats 5.17 % of python3 submissions (13.6 MB)
'''
        

