#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (49.46%)
# Likes:    1469
# Dislikes: 247
# Total Accepted:    214.6K
# Total Submissions: 433.9K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Note:
# 
# 
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be
# at least a next smallest number in the BST when next() is called.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        if root:
            self.stack = [root]
        else:
            self.stack = []
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.stack:
            first = self.stack.pop(0)
            
            new_head = [first]
            if first.left:
                new_head.insert(0, first.left)
                first.left = None
            if first.right:
                new_head.append(first.right)
                first.right = None
            if len(new_head) == 1:
                return first.val
            else:
                self.stack = new_head + self.stack
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
'''
Runtime: 88 ms, faster than 79.18% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 20.4 MB, less than 5.02% of Python3 online submissions for Binary Search Tree Iterator.
'''

