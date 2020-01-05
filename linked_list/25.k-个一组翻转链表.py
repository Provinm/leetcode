#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(start, end):

            if start is end:
                return end

            next_node = reverse(start.next, end)

            start.next = None
            next_node.next = start

            return start

        if not head:
            return head

        temp = k
        start, ptr = head, head
        ret = None
        conn = None
        while ptr:

            temp -= 1
            if temp == 0:
                _s, _e = start, ptr
                start = ptr.next
                ptr = ptr.next
                # print(f"s = {_s.val}, e= {_e.val}")
                reverse(_s, _e)
                if conn:
                    conn.next = _e
                conn = _s
                temp = k
                if not ret:
                    ret = _e

                continue

            ptr = ptr.next

            if conn:
                conn.next = start

        return ret or head


"""

Accepted
81/81 cases passed (48 ms)
Your runtime beats 94.2 % of python3 submissions
Your memory usage beats 42.28 % of python3 submissions (14.2 MB)



"""
# @lc code=end

