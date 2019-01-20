#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (34.78%)
# Total Accepted:    161.4K
# Total Submissions: 464.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k < 2:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        f_ptr = l_ptr = dummy
        

        while f_ptr:
            
            # 移动 f_ptr k 次
            count = k
            while count and f_ptr.next:
                count -= 1
                f_ptr = f_ptr.next

            if count:
                break

            # 移动 l_ptr 完成翻转
            cur_node = l_ptr.next
            l_ptr.next = f_ptr
            next_node = cur_node.next
            cur_node.next = f_ptr.next
            print("=========== l ptr ==========")
            print_nodes(l_ptr)
            print("=========== cur node ==========")
            print_nodes(cur_node)
            print("=========== next node ==========")
            print_nodes(next_node)

            count = k
            while count:
                count -= 1
                temp = next_node.next
                next_node.next = cur_node
                cur_node = next_node
                next_node = temp

            l_ptr = f_ptr

        return dummy.next


def print_nodes(head):

    res = []
    while head:
        res.append(head.val)
        head = head.next

    print(res)


def gen_head(lst):

    head = node = ListNode(lst.pop(0))

    while lst:
        item = lst.pop(0)
        node.next = ListNode(item)
        node = node.next

    return head
            

head = gen_head([1,2,3,4,5])
k = 2

s = Solution()
print_nodes(s.reverseKGroup(head, k))
            
        
