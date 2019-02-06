#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (52.75%)
# Total Accepted:    166K
# Total Submissions: 314.8K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#

import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dct = {}
        for num in nums:
            if num in dct:
                dct[num] += 1
            dct.setdefault(num, 1)

        heaps = [(-value, key) for key, value in dct.items()]

        heapq.heapify(heaps)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heaps)[1])
        return res

# nums = [1,1,1,2,2,3]
# k = 2
# s = Solution()
# print(s.topKFrequent(nums, k))

'''

time O(n) + O(N) + O(k)
space O(n) + O(n)

✔ Accepted
✔ 21/21 cases passed (52 ms)
✔ Your runtime beats 42.73 % of python3 submissions
'''

