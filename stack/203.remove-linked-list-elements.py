#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (36.25%)
# Likes:    920
# Dislikes: 57
# Total Accepted:    242.3K
# Total Submissions: 668.5K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        cur = ret = ListNode(None)
        while head:
            if head.val != val:
                cur.next = head
                cur = cur.next
            head = head.next

        cur.next = None
        return ret.next

'''
√ Accepted
  √ 65/65 cases passed (72 ms)
  √ Your runtime beats 86.18 % of python3 submissions
  √ Your memory usage beats 5.55 % of python3 submissions (17 MB)

'''
