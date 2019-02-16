#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (35.18%)
# Total Accepted:    226.9K
# Total Submissions: 644.9K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':

        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        return lst == lst[::-1]

'''
time O(n) space O(n)

✔ Accepted
✔ 26/26 cases passed (72 ms)
[WARN] Failed to get submission beat ratio.

'''
