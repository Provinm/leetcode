#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (55.97%)
# Total Accepted:    99.6K
# Total Submissions: 178K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
# 
# Example:
# 
# 
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# 
# Note:
# 
# 
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
# 
#
class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':

        xor = 0
        for i in nums:
            xor ^= i
        xor &= -xor # get the last 1 of xor: 10101000 -> 1000
        a, b = 0, 0
        for i in nums: # devide the numbers into two parts, and a, b should be divided into different part
            if i & xor:
                a ^= i
            else: 
                b ^= i
        return [a, b]
    # S 1
    # def singleNumber(self, nums: 'List[int]') -> 'List[int]':

    #     dct = {}
    #     for ele in nums:
    #         if ele in dct:
    #             del dct[ele]
    #         else:
    #             dct[ele] = 1

    #     return list(dct.keys())

    
'''
解法一，通俗易懂但是 time  O(n) space O(n)
√ Accepted
√ 30/30 cases passed (36 ms)
[WARN] Failed to get submission beat ratio.

解题思路：
1、首先为了解决这个问题,需要采取一种办法让整个 list 分为两拨,两个数字分别在两个数组中，这样对两个数组分别 ^ 得到最后的结果
2、任何两个数从右往左数第一位 异，比如  4(0100) 3(0011) 为 1， 9(1001) 和 5(0101) 为 4
3、只需要找到第一位 异， 然后进行 & 运算，这两个数会得到 0 或 1，以此来将两数分在不同的组内，比如 4&1 = 0， 3&1 = 1
4、然后来找第一位 异，需要对两位进行 异或 运算，然后 & 其的负数
讲真我也是一知半解，我自己肯定写不出来这样的代码，只能先理解下来
√ Accepted
√ 30/30 cases passed (40 ms)
[WARN] Failed to get submission beat ratio.
'''
