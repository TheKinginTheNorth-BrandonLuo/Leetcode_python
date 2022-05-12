# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:16:01 2022

@author: Fan Luo
"""
"""
334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
"""
class Solution:
    def increasingTriplet(self, nums):
        # method 1: two pointers
        p1, p2 = float("inf"), float("inf")
        
        for n in nums:
            if n <= p1:
                p1 = n
            elif n <= p2:
                p2 = n
            else:
                return True
        return False