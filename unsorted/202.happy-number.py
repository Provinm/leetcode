#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (46.13%)
# Likes:    969
# Dislikes: 251
# Total Accepted:    254.3K
# Total Submissions: 551.3K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
#
# Example:
#
#
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
class Solution:
    def isHappy(self, n: int) -> bool:

        if n < 5:
            return n == 1

        temp_sum = 0
        while n:
            temp = n % 10
            temp_sum += temp ** 2
            n = n // 10

        return self.isHappy(temp_sum)


# s = Solution()
# r = s.isHappy(4)
# print(r)
"""
√ Accepted
  √ 401/401 cases passed (32 ms)
  √ Your runtime beats 98.81 % of python3 submissions
  √ Your memory usage beats 5.26 % of python3 submissions (13.7 MB)

  """
