#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (35.82%)
# Total Accepted:    148K
# Total Submissions: 413.1K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        dummy.next = head

        pre_node = min_node = dummy
        cur_node = head

        while cur_node:

            if cur_node.val < x:

                if min_node is pre_node:
                    min_node = pre_node = cur_node
                    cur_node = cur_node.next
                else:
                    temp = min_node.next
                    next_node = cur_node.next

                    min_node.next = cur_node
                    min_node = min_node.next

                    cur_node.next = temp
                    cur_node = next_node

                    pre_node.next = next_node

            else:

                pre_node = cur_node
                cur_node = cur_node.next

        return dummy.next

        
'''

这他么就尴尬了, 时间复杂度是 O(n) 空间复杂度为 0(1) 怎么才击败 5.93% 

  ✔ Accepted
  ✔ 166/166 cases passed (92 ms)
  ✔ Your runtime beats 5.93 % of python3 submissions

'''
