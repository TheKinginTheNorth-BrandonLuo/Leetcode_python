# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:39:33 2022

@author: Fan Luo
"""
"""
164. Maximum Gap

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. 
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
"""

from collections import defaultdict

class Solution:
    def maximumGap(self, nums):
        low, high, N = min(nums), max(nums), len(nums)
        
        if N <= 2 or low == high:
            return high - low
        
        bucket = defaultdict(list)
        
        for n in nums:
            ind = N -2 if n == high else (n - low) *(N - 1) //(high - low)
            bucket[ind].append(n)
            
        res = [[min(bucket[i]), max(bucket[i])] for i in range(N - 1) if bucket[i]]
        return max(y[0] - x[1] for x, y in zip(res, res[1:]))