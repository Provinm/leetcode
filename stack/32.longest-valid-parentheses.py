#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (24.65%)
# Total Accepted:    165.8K
# Total Submissions: 672.7K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_length = 0

        stack = [(s[0], 0)]
        stack_valid = []
        dct = {"(": ")"}

        for idx, word in enumerate(s[1:], 1):
            if word in dct:
                stack.append((word, idx))
            else:
                if stack and stack[-1][0] in dct:
                    stack_valid.append(stack.pop()[1])
                    stack_valid.append(idx)
                else:
                    stack.append((word, idx))

        if not stack_valid:
            return 0
        
        stack_valid.sort()
        cur_length = 1
        while len(stack_valid) > 1:
            item = stack_valid.pop()
            if item - stack_valid[-1] == 1:
                cur_length += 1
            else:
                max_length = max(max_length, cur_length)
                cur_length = 1
        else:
            max_length = max(max_length, cur_length)

        return max_length
            
# st = "(()))())("
# s = Solution()
# print(s.longestValidParentheses(st))

'''

时间复杂度为 O(nlogn) 不算最好算法
  √ Accepted
  √ 230/230 cases passed (108 ms)
  √ Your runtime beats 21.04 % of python3 submissions

'''