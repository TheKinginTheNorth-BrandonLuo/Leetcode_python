# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:55:28 2022

@author: Fan Luo
"""
"""
674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
"""
class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        for i in range(1, len(dp)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                
        return max(dp)