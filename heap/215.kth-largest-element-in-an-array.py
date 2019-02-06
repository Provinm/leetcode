#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (45.16%)
# Total Accepted:    307K
# Total Submissions: 679.8K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 最小堆
        min_heaps = nums[:k]
        heapq.heapify(min_heaps)
        for idx in range(k, len(nums)):
            item = nums[idx]
            if item > min_heaps[0]:
                heapq.heappop(min_heaps)
                heapq.heappush(min_heaps, item)

        return min_heaps[0]
            
        
    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """

    #     # 最大堆
    #     nums = [-num for num in nums]
    #     heapq.heapify(nums)

    #     res = None
    #     for i in range(k):
    #         res = heapq.heappop(nums)

    #     return -res



    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """

    #     heapq.heapify(nums)

    #     k = len(nums) - k + 1

    #     res = None
    #     while k:
    #         k -= 1
    #         res = heapq.heappop(nums)

    #     return res



# nums = [3,2,1,5,6,4]
# k = 2
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
# s = Solution()
# print(s.findKthLargest(nums, k))

'''
最小堆的实现 

✔ Accepted
✔ 32/32 cases passed (56 ms)
✔ Your runtime beats 34.42 % of python3 submissions


本题为常考题目，需要了解最大堆，最小堆的区别

'''

        
