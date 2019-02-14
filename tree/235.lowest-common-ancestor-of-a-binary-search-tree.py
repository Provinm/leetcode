#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (43.17%)
# Total Accepted:    252.9K
# Total Submissions: 585.8K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# 
# 
# Example 2:
# 
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# 
# 
# Note:
# 
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
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
    # solution3
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root


    # solution 1
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """

    #     if not root or root.val == p.val or root.val == q.val:
    #         return root

    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)

    #     if left and right:
    #         return root

    #     elif left:
    #         return left

    #     elif right:
    #         return right

    #     else:
    #         return None

    
            
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """

    #     def sub(root, p, q):

    #         lr = rr = [None, 0]

    #         if root.left:
    #             lr = sub(root.left, p, q)
    #             if lr[1] == 2:
    #                 return lr
            
    #         if root.right:
    #             rr = sub(root.right, p, q)
    #             if rr[1] == 2:
    #                 return rr

    #         if root.val == p.val or root.val == q.val:
    #             if lr[1] == 0:
    #                 lr = [root, 1]
    #             else:
    #                 rr = [root, 1]

    #         if lr[1] == rr[1] == 1:
    #             return [root, 2]

    #         elif lr[1] == 1 or rr[1] == 1:
    #             return [root, 1]

    #         else:
    #             return lr

    #     return sub(root, p, q)[0]


'''
解法一　time O(n) space O(1)

✔ Accepted
✔ 27/27 cases passed (100 ms)
[WARN] Failed to get submission beat ratio.


解法二　time O(n) space O(1)
比一快的一点在于进行了剪枝
✔ Accepted
✔ 27/27 cases passed (96 ms)
[WARN] Failed to get submission beat ratio.



解法三，利用了 b t 的性质， time O(logn) space O(1)
✔ Accepted
  ✔ 27/27 cases passed (80 ms)
[WARN] Failed to get submission beat ratio.

'''
        
