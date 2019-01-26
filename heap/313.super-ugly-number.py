#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (40.21%)
# Total Accepted:    55.4K
# Total Submissions: 137.8K
# Testcase Example:  '12\n[2,7,13,19]'
#
# Write a program to find the nth super ugly number.
# 
# Super ugly numbers are positive numbers whose all prime factors are in the
# given prime list primes of size k.
# 
# Example:
# 
# 
# Input: n = 12, primes = [2,7,13,19]
# Output: 32 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12 
# ⁠            super ugly numbers given primes = [2,7,13,19] of size 4.
# 
# Note:
# 
# 
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
# 
# 
#
import heapq
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        
        factors = primes[:]

        # r = 1
        heapq.heapify(factors)
        for _ in range(2, n+1):

            ele = heapq.heappop(factors)
            for p in primes:
                if ele*p not in factors:
                    heapq.heappush(factors, ele*p)
            # if ele*2 not in factors:
            #     heapq.heappush(factors, ele*2)

            # if ele*3 not in factors:
            #     heapq.heappush(factors, ele*3)

            # if ele*5 not in factors:
            #     heapq.heappush(factors, ele*5)

        return ele

# n = 12
# primes = [2,7,13,19]
# s = Solution()
# print(s.nthSuperUglyNumber(n,primes))
