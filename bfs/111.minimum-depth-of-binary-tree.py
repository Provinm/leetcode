#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (34.69%)
# Total Accepted:    266.5K
# Total Submissions: 768.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
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
# return its minimum depth = 2.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        res = 0
        stack = [root]
        while stack:
            res += 1
            new_stack = []
            while stack:
                node = stack.pop(0)

                if not node.left and (not node.right):
                    return res
                
                if node.left:
                    new_stack.append(node.left)

                if node.right:
                    new_stack.append(node.right)

            stack = new_stack

        return res


'''
BFS,time(worst) O(n) space(worst) O(n)

√ Accepted
√ 41/41 cases passed (56 ms)
√ Your runtime beats 27.27 % of python3 submissions
'''
        
