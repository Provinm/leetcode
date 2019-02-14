#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (27.43%)
# Total Accepted:    284.6K
# Total Submissions: 1M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (xn).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]
# 
# 
#
class Solution:
    def myPow(self, x: 'float', n: 'int') -> 'float':

        if n == 0:
            return 1

        if n < 0:
            return self.myPow(1/x, -n)

        if n % 2 == 1:
            return x * self.myPow(x*x, (n-1)//2)
        
        else:
            return self.myPow(x*x, n//2)
        

'''

✔ Accepted
✔ 304/304 cases passed (36 ms)
[WARN] Failed to get submission beat ratio.

'''
