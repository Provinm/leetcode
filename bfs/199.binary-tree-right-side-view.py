#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (46.09%)
# Total Accepted:    145.4K
# Total Submissions: 315.5K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        stack = [root]
        while stack:

            new_stack = []
            while stack:
                node = stack.pop(0)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)

            res.append(node.val)
            stack = new_stack

        return res

                

'''
BFS time O(n), space O(k) 最长一层的个数

√ Accepted
√ 211/211 cases passed (40 ms)
√ Your runtime beats 34.38 % of python3 submissions
''' 
                
            

