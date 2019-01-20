#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (38.67%)
# Total Accepted:    190.9K
# Total Submissions: 493.7K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if not inorder:
            return None

        root_item = preorder.pop(0)
        root = TreeNode(root_item)

        root_index = inorder.index(root_item)

        inorder_lefts = inorder[:root_index]
        inorder_rights = inorder[root_index+1:]

        preorder_lefts = preorder[:len(inorder_lefts)]
        preorder_rights = preorder[len(inorder_lefts):]


        root.left = self.buildTree(preorder_lefts, inorder_lefts)
        root.right = self.buildTree(preorder_rights, inorder_rights)

        return root

'''

DFS 时间复杂度为 O(n) 每个节点都会走一遍

  ✔ Accepted
  ✔ 203/203 cases passed (260 ms)
  ✔ Your runtime beats 53.28 % of python3 submissions

'''
