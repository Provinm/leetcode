#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (40.45%)
# Total Accepted:    211.7K
# Total Submissions: 523.3K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        
        # stack
        # preorder 
        stack = []

        def sub(root, stack):

            stack.append(root)
            if root.left:
                sub(root.left, stack)

            if root.right:
                sub(root.right, stack)

        sub(root, stack)

        while len(stack) > 1:

            stack[-1].right = stack.pop()
            stack[-1].left = None

        # return stack[0]

'''
时间复杂度为 O(N) 空间复杂度为 O(N) 

  ✔ Accepted
  ✔ 225/225 cases passed (76 ms)
  ✔ Your runtime beats 30.18 % of python3 submissions



'''