#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (50.36%)
# Total Accepted:    320.4K
# Total Submissions: 636.4K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        
        nums.sort()

        def sub(nums):

            if not nums:
                return [[]]

            res = [[]]
            for idx, ele in enumerate(nums):
                if idx>0 and ele == nums[idx-1]:
                    continue
                res.append([ele])
                temp = sub(nums[idx+1:])
                for item in temp:
                    if item:
                        res.append([ele] + item)
            return res

        res = sub(nums)
        # res.sort(reverse=True)
        return res

# nums = [1,2,3]

# s = Solution()
# r = s.subsets(nums)

# print(r)

'''

time O(nlogn) + O(n**2) -> O(n**2)
space O(n**2)
✔ Accepted
✔ 10/10 cases passed (40 ms)
[WARN] Failed to get submission beat ratio.

'''