# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:37:22 2022

@author: Fan Luo
"""
"""
324. Wiggle Sort II

Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
"""
class Solution:
    def wiggleSort(self, nums):
        res = sorted(nums)
        
        for i in range(1, len(nums), 2):
            nums[i] = res.pop()
        for i in range(0, len(nums), 2):
            nums[i] = res.pop()