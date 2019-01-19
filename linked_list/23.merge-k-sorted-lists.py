#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (32.13%)
# Total Accepted:    319.6K
# Total Submissions: 995K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # HEAP 
        import heapq
        
        res = []
        count = 0
        while lists:
            head = lists.pop(0)
            while head:
                res.append((head.val, count, head))
                head = head.next
                count += 1

        heapq.heapify(res)

        head = node = None
        while res:

            item = heapq.heappop(res)[2]
            if not head:
                head = node = item
            else:
                node.next = item
                node = node.next

        return head

'''

维护一个最小堆

  ✔ Accepted
  ✔ 131/131 cases passed (136 ms)
  ✔ Your runtime beats 58.85 % of python3 submissions

'''