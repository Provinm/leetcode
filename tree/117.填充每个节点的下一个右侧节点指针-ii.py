#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root
        stack = [root]

        while stack:

            temp = []
            stack[-1].next = None
            while stack:
                ele = stack.pop(0)
                if stack:
                    ele.next = stack[0]
                if ele.left:
                    temp.append(ele.left)
                if ele.right:
                    temp.append(ele.right)

            stack = temp

        return root


# @lc code=end

"""
Accepted
55/55 cases passed (88 ms)
Your runtime beats 64.93 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (13.9 MB)

做法和 116 一样
"""

