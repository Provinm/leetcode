#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (30.90%)
# Total Accepted:    144.3K
# Total Submissions: 466.7K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# Note:
# 
# 
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
# 
# 
# Example 1:
# 
# 
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
#
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        if not tokens:
            return 0

        stack = []
        import operator
        mapping = {"+": operator.add, "-": operator.sub, "/":operator.truediv, "*": operator.mul}

        for idx, item in enumerate(tokens):

            if item in mapping:
                right = stack.pop(-1)
                left = stack.pop(-1)
                # print(f"{left} {item} {right}")
                stack.append(int(mapping[item](left, right)))
            
            else:
                stack.append(int(item))
        # print(stack)
        return stack[-1]
        
# l = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# s = Solution()
# print(s.evalRPN(l))
'''

经典的 stack 题目　时间复杂度为　O(n), 空间复杂度为 O(n)　使用了 stack 存值
  ✔ Accepted
  ✔ 20/20 cases passed (64 ms)
  ✔ Your runtime beats 58.13 % of python3 submissions


'''