#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (39.80%)
# Total Accepted:    185.7K
# Total Submissions: 466.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # DFS
        
        res = []
        self.sub(root, 0, res)
        return res


    def sub(self, root, deepth=0, res=[]):

        if not root:
            return None

        if len(res) == deepth:
            res.append([])

        if deepth % 2 == 0:
            res[deepth].append(root.val)
        else:
            res[deepth].insert(0, root.val)

        if root.left:
            self.sub(root.left, deepth+1, res)
        if root.right:
            self.sub(root.right, deepth+1, res)

    # def zigzagLevelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
        
    #     # BFS

    #     res = []
    #     if not root:
    #         return res
        
    #     stack = [root]
    #     count = 0
    #     while stack:
            
    #         temp_res = []
    #         new_stack = []
    #         # zero_or_one = 0 if count // 2 else -1
    #         while stack:
    #             node = stack.pop(0)
    #             temp_res.append(node.val)
    #             if node.left:
    #                 new_stack.append(node.left)

    #             if node.right:
    #                 new_stack.append(node.right)

    #         if count % 2 == 0:
    #             res.append(temp_res)
    #         else:
    #             res.append(temp_res[::-1])
    #         count += 1
    #         stack = new_stack

    #     return res

'''  
BFS O(n)
✔ Accepted
✔ 33/33 cases passed (56 ms)
✔ Your runtime beats 71.86 % of python3 submissions

DFS O(n)
✔ Accepted
✔ 33/33 cases passed (56 ms)
✔ Your runtime beats 71.86 % of python3 submissions

由于时间复杂度都是 O(n)　所以用时相同

'''