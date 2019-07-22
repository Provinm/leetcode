#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (36.65%)
# Total Accepted:    65.7K
# Total Submissions: 179.4K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# Example:
# 
# 
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# 
#

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        dct = {}

        for idx, ele in enumerate(nums):
            if ele in dct:
                dct[ele].append(idx)
            else:
                dct[ele] = [idx]

        nums.sort(reverse=True)
        length = len(nums)
        res = [0 for _ in nums]
        
        jdx = 0
        while jdx < length:

            item = nums[jdx]
            raw_idx = idx = dct[item].pop(0)

            while dct[item] and dct[item][0]-idx == 1:
                jdx += 1
                idx = dct[item].pop(0)

            if idx >= jdx:
                temp = length - idx - 1 - len(dct[item])
            else:
                temp = length - jdx - 1 - len(dct[item])

            while raw_idx <= idx:
                res[raw_idx] = temp
                raw_idx += 1

            jdx += 1

        return res


nums = [5,2,2,6,1,5,5,5]
s = Solution()
print(s.countSmaller(nums))

'''

O(n**2) 的算法超时



'''