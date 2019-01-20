#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (38.87%)
# Total Accepted:    205.8K
# Total Submissions: 529.4K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
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
# ⁠/  \    / \
# 7    2  5   1
# 
# 
# Return:
# 
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        cur_lst = []
        res_lst = []

        self.sub(root, sum, cur_lst, res_lst)
        return res_lst

    def sub(self, root, _sum, cur_lst, res_lst):

        if not root.left and not root.right:
            cur_lst.append(root.val)
            # print(f"a after append {cur_lst}")
            if sum(cur_lst) == _sum:
                res_lst.append(cur_lst[:])
            cur_lst.pop()
            # print(f"a after pop {cur_lst}")
            return 

        # if sum(cur_lst) + root.val > _sum:
        #     return

        cur_lst.append(root.val)
        # print(f"after append {cur_lst}")
        if root.left:
            self.sub(root.left, _sum, cur_lst, res_lst)

        if root.right:
            self.sub(root.right, _sum, cur_lst, res_lst)
        cur_lst.pop()
        # print(f"after pop {cur_lst}")

'''

DFS 时间复杂度为 O(N)
  ✔ Accepted
  ✔ 114/114 cases passed (60 ms)
  ✔ Your runtime beats 96.9 % of python3 submissions

'''