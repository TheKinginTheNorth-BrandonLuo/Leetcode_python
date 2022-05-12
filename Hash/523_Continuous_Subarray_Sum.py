# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:26:27 2022

@author: Fan Luo
"""
"""
523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
"""
class Solution:
    def checkSubarraySum(self, nums, k):
        remainder = {0:-1}
        total = 0
        
        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1: # avoid 0 case 
                # which means remainder happens twice and it must have added an k to make same remainder
                # eg 23 % 6 =5, while 29 % 6 = 5
                # means we already added an k into it
                return True
        return False