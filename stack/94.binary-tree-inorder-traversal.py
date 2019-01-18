#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (54.16%)
# Total Accepted:    387.4K
# Total Submissions: 714.8K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 迭代法就牛逼了
        # 要将某个节点有序输出，必须遍历某个节点两次
        #　第一次安排位置，第二次取出元素

        res = []
        if not root:
            return res
        
        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()

            # 未访问过
            if node not in visited:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                if node.left:
                    stack.append(node.left)

                visited.add(node)

            else:
                res.append(node.val)
            
        return res

    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """

    #     #  left root　right
    #     res = []
    #     if not root:
    #         return res
    #     res.extend(self.inorderTraversal(root.left))
    #     res.append(root.val)
    #     res.extend(self.inorderTraversal(root.right))
    #     return res
            

'''

recursion 

✔ Accepted
✔ 68/68 cases passed (52 ms)
✔ Your runtime beats 75.51 % of python3 submissions

iterative

✔ Accepted
✔ 68/68 cases passed (68 ms)
✔ Your runtime beats 9.76 % of python3 submissions


啧啧啧, 迭代法由于时间复杂度为　O(2n) 空间复杂度为 O(n) 表现差也在意料之中

'''