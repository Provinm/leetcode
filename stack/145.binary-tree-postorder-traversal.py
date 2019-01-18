#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (46.07%)
# Total Accepted:    226.2K
# Total Submissions: 490.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
#   
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [3,2,1]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 和中序遍历的迭代算法异曲同工之妙
        res = []

        if not root:
            return res

        stack = [root]
        visited = set()

        while stack:

            node = stack.pop()
            if node not in visited:
                stack.append(node)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                visited.add(node)
            else:
                res.append(node.val)

        return res

'''

时间复杂度为 O(2n) 每个节点访问两次　空间复杂度为 O(n) 
  ✔ Accepted
  ✔ 68/68 cases passed (56 ms)
  ✔ Your runtime beats 41.88 % of python3 submissions

'''
