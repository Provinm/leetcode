#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (25.25%)
# Total Accepted:    361.7K
# Total Submissions: 1.4M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's
# value
# is 5 but its right child's value is 4.
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
    def isValidBST(self, root: TreeNode) -> bool:

        
        def sub(root, res):
            if not root:
                return 
            
            if root.left:
                sub(root.left, res)

            res.append(root.val)

            if root.right:
                sub(root.right, res)


        res = []
        sub(root, res)

        return res == sorted(set(res))

'''

time O(nlogn) space O(n)


✔ Accepted
  ✔ 75/75 cases passed (68 ms)
  ✔ Your runtime beats 23.85 % of python3 submissions
  ✔ Your memory usage beats 5.14 % of python3 submissions (17 MB)
'''

