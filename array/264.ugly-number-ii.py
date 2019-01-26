#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (35.18%)
# Total Accepted:    93.8K
# Total Submissions: 266.6K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#
import heapq
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        
        factors = [2,3,5]

        r = 1
        heapq.heapify(factors)
        for _ in range(2, n+1):

            ele = heapq.heappop(factors)
            if ele*2 not in factors:
                heapq.heappush(factors, ele*2)

            if ele*3 not in factors:
                heapq.heappush(factors, ele*3)

            if ele*5 not in factors:
                heapq.heappush(factors, ele*5)

        return ele


# n = 11
# s = Solution()
# print(s.nthUglyNumber(n))
'''
时间复杂度为 O(n**2)

  ✔ Accepted
  ✔ 596/596 cases passed (1072 ms)
  ✔ Your runtime beats 12.19 % of python3 submissions

'''