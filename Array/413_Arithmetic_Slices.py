# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:38:56 2022

@author: Fan Luo
"""
"""
413. Arithmetic Slices

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
"""
class Solution:
    def numberOfArithmeticSlices(self, nums):
        res = 0
        t = 1
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                # for [1,2,3], add 4 to the end will cause more situations
                # that time we need to add 2 not 1
                # which also means we need to add 1 to t
                res += t
                t += 1
            else:
                t = 1
        return res
