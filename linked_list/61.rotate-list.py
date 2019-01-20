#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (26.17%)
# Total Accepted:    171.3K
# Total Submissions: 654.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # 解法二
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not head.next or k == 0:
            return head

        count = 1
        tail = head
        while tail.next:
            tail = tail.next
            count += 1
        
        k = k % count 
        p = abs(count-k)

        tail.next = head

        while p>1:
            p -= 1
            head = head.next

        r = head.next
        head.next = None

        return r
        

        
    
    # 解法一
    # def rotateRight(self, head, k):
    #     """
    #     :type head: ListNode
    #     :type k: int
    #     :rtype: ListNode
    #     """

    #     if not head or not head.next or k == 0:
    #         return head
    #     stack1 = []
    #     stack2 = []

    #     count = 0
    #     while head:
    #         stack1.append(head)
    #         head = head.next
    #         count += 1

    #     k = k % count
    #     while k:
    #         stack2.append(stack1.pop())
    #         k -= 1
    #     if stack1 and stack2:
    #         stack1[-1].next = None
    #         stack2[0].next = stack1[0]
    #         head = stack2[-1]
    #     elif stack1:
    #         head = stack1[0]

    #     elif stack2:
    #         head = stack2[-1]

    #     return head

'''
解法一
时间复杂度在最坏的情况下是 O(2n), 空间复杂度也是 O(n)

  ✔ Accepted
  ✔ 231/231 cases passed (76 ms)
  ✔ Your runtime beats 30.82 % of python3 submissions

解法二 O(n)　空间复杂度为　O(1)

  ✔ Accepted
  ✔ 231/231 cases passed (72 ms)
  ✔ Your runtime beats 41.88 % of python3 submissions


'''
        
