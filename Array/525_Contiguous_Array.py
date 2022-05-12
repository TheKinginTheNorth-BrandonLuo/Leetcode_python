# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 22:27:53 2022

@author: jiarong xia
"""
"""
525. Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
"""

class Solution:
    def findMaxLength(self, nums):
        lookup = {}
        cum_sum, max_len = 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                cum_sum -= 1
            else:
                cum_sum += 1
                
            if cum_sum == 0:
                max_len = i + 1
            elif cum_sum in lookup:
                max_len = max(max_len, i - lookup[cum_sum])
            else:
                lookup[cum_sum] = i
                
        return max_len