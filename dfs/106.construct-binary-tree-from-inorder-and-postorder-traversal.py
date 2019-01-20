#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (37.29%)
# Total Accepted:    135.6K
# Total Submissions: 363.6K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not inorder:
            return None

        root_item = postorder.pop()
        root = TreeNode(root_item)

        root_index = inorder.index(root_item)

        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index+1:]

        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root

'''
和 105 相同，用时长的原因应该是空间复杂度高， 如果 in-place 操作可能会好一点
但是会增加代码阅读难度

  ✔ Accepted
  ✔ 203/203 cases passed (360 ms)
  ✔ Your runtime beats 19.78 % of python3 submissions

'''
        
