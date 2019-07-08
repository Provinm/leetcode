#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (41.36%)
# Likes:    1067
# Dislikes: 68
# Total Accepted:    181.2K
# Total Submissions: 438K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        def sub(s):

            if not s:
                return None

            length = len(s)
            mid = length // 2
            tree = TreeNode(s[mid])
            tree.left = sub(s[:mid])
            tree.right = sub(s[mid+1:])

            return tree

        return sub(stack)


'''

√ Accepted
  √ 32/32 cases passed (124 ms)
  √ Your runtime beats 93.14 % of python3 submissions
  √ Your memory usage beats 42.15 % of python3 submissions (19.7 MB)

'''
