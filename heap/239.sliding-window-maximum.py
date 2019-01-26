#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (36.57%)
# Total Accepted:    129.6K
# Total Submissions: 354.5K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# 
# Example:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
# 
# Follow up:
# Could you solve it in linear time?
# 
#

import heapq
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums or k == 1 or k == 0:
            return nums

        windows = []
        res = []
        for idx, item in enumerate(nums):
            
            # 右滑删除 windows 中过期元素
            if windows and idx - windows[0] >= k:
                windows.pop(0)

            # 删除 windows 中比 item 小的元素
            while windows and nums[windows[-1]] <= item:
                windows.pop()

            # 添加元素
            windows.append(idx)

            # 向结果中添加元素
            if idx >= k - 1:
                res.append(nums[windows[0]])
            
        return res

    
# heapq.heappushpop()

# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# nums = [7,2,4]
# k = 2
# nums = [4, 3, 11]
# k = 3
# nums = [1,3,1,2,0,5]
# k = 3
# s = Solution()
# print(s.maxSlidingWindow(nums,k))
        
'''

时间复杂度为 O(N) 空间复杂度为 O(k)

✔ Accepted
✔ 18/18 cases passed (112 ms)
✔ Your runtime beats 58 % of python3 submissions


'''