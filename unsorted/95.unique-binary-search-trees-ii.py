#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (34.83%)
# Total Accepted:    128.9K
# Total Submissions: 370.2K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        if n < 1:
            return []

        lst = list(range(1, n+1))

        def sub(lst):

            if not lst:
                return [None]

            res = []
            for idx, item in enumerate(lst):

                left = lst[:idx]
                right = lst[idx+1:]
                left_lst = sub(left)
                right_lst = sub(right)

                for left_node in left_lst:
                    for right_node in right_lst:
                        node = TreeNode(item)
                        node.left = left_node
                        node.right = right_node
                        res.append(node)
            
            return res

        res = sub(lst)
        return res
            

'''
DFS time  O(n**2)
√ Accepted
  √ 9/9 cases passed (64 ms)
  √ Your runtime beats 58.59 % of python3 submissions
  √ Your memory usage beats 5.35 % of python3 submissions (15 MB)
'''


        
