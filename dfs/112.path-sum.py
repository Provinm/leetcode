#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (36.68%)
# Total Accepted:    274.4K
# Total Submissions: 748K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        if not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False

        if root.left:
            root.left.val += root.val
            if self.hasPathSum(root.left, sum):
                return True

        if root.right:
            root.right.val += root.val
            if self.hasPathSum(root.right, sum):
                return True

        return False

        
'''

最差的时间复杂度为 O(n) 
  ✔ Accepted
  ✔ 114/114 cases passed (80 ms)
  ✔ Your runtime beats 47.63 % of python3 submissions


'''