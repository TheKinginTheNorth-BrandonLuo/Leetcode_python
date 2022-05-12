# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 23:31:36 2022

@author: Fan Luo
"""
"""
152. Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""

class Solution:
    def maxProduct(self, nums):
        pos, neg, res = nums[0], nums[0],nums[0]
        
        for i in nums[1:]:
            pos, neg = max(i, pos * i, neg * i), min(i, pos * i, neg * i)
            res = max(res, pos)
            
        return res