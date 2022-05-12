# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:45:20 2022

@author: Fan Luo
"""
"""
368. Largest Divisible Subset

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
"""
class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        N = len(nums)
        if N < 2:
            return nums
        
        res = [[n] for n in nums]
        
        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(res[i]) < len(res[j]) + 1:
                    res[i] = res[j] + [nums[i]]
                    
        return max(res, key = lambda x: len(x))