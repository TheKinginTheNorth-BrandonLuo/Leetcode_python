# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 20:59:38 2022

@author: Fan Luo
"""
"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, 
    so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""
class Solution:
    def missingNumber(self, nums):
        largest = len(nums)
        return int(largest * (largest + 1) / 2 - sum(nums))