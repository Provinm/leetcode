#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (31.82%)
# Total Accepted:    163.2K
# Total Submissions: 512.8K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        target = head.val
        dummy = ListNode(-1)
        dummy.next = head

        pre_node = dummy
        cur_node = head
        next_node = head.next

        delete_cur = False
        while next_node:

            if next_node.val == cur_node.val:
                cur_node.next = next_node.next
                next_node = next_node.next
                delete_cur = True

            else:
                if delete_cur:
                    pre_node.next = next_node
                    # cur_node = next_node
                    # next_node = next_node.next
                    delete_cur = False
                else:
                    pre_node = cur_node
                cur_node = next_node
                next_node = next_node.next

        else:
            if delete_cur:
                pre_node.next = next_node


        return dummy.next

'''
时间复杂度为 O(n) 实在想不到还有比这个更好的算法了

  ✔ Accepted
  ✔ 168/168 cases passed (76 ms)
  ✔ Your runtime beats 49.09 % of python3 submissions

本题还可以用 stack 来做,但是由于空间复杂度为 O(n) 时间复杂度为 0(2n) 肯定不如上面的解法

'''

        
