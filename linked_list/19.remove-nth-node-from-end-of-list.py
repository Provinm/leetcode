#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (33.85%)
# Total Accepted:    336.2K
# Total Submissions: 993.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        stack = []

        while head:
            stack.append(head)
            head = head.next

        stack.pop(-n)
        stack.append(None)

        # ptr = 0
        # while ptr < len(stack):
        #     stack[ptr].next = stack[ptr+1]
        while len(stack) > 1:
            stack[-1].next = stack.pop()

        return stack[0]

    # def removeNthFromEnd(self, head, n):
    #     """
    #     :type head: ListNode
    #     :type n: int
    #     :rtype: ListNode
    #     """
    #     dummy = ListNode(-1)
    #     dummy.next = head

    #     f_ptr = l_ptr = dummy

    #     while f_ptr.next:
    #         if n == 0:
    #             l_ptr = l_ptr.next
    #         else:
    #             n -= 1
    #         f_ptr = f_ptr.next
    #     else:
    #         l_ptr.next = l_ptr.next.next

    #     return dummy.next

'''

O(n) 的复杂度，　慢应该是新建了一个 dummy node

✔ Accepted
✔ 208/208 cases passed (68 ms)
✔ Your runtime beats 33.16 % of python3 submissions


使用 stack 时间复杂度为 O(2n) 所以慢也是合理的
✔ Accepted
✔ 208/208 cases passed (88 ms)
[WARN] Failed to get submission beat ratio.

'''

        
