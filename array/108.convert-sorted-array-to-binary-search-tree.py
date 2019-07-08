#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (51.40%)
# Likes:    1210
# Dislikes: 128
# Total Accepted:    273K
# Total Submissions: 531.3K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def sub(s):

            if not s:
                return None

            length = len(s)
            mid = length // 2
            tree = TreeNode(s[mid])
            tree.left = sub(s[:mid])
            tree.right = sub(s[mid+1:])

            return tree

        return sub(nums)

'''

√ Accepted
  √ 32/32 cases passed (60 ms)
  √ Your runtime beats 89.89 % of python3 submissions
  √ Your memory usage beats 35.87 % of python3 submissions (15.6 MB)


'''
