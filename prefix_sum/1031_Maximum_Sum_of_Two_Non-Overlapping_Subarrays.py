# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:27:38 2022

@author: Fan Luo
"""
"""
1031. Maximum Sum of Two Non-Overlapping Subarrays

Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

A subarray is a contiguous part of an array.

Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
"""
class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        prefix = [0]
        maxFirst, maxSecond, res = 0, 0, 0
        for i in nums:
            prefix.append(prefix[-1] + i)
            
        # assume firstlen happens after secondLen
        for i in range(secondLen, len(prefix) - firstLen):
            maxSecond = max(maxSecond, prefix[i] - prefix[i - secondLen])
            res = max(res, maxSecond + prefix[i + firstLen] - prefix[i])
            
        # assume firstLen happens before secondLen
        for i in range(firstLen, len(prefix) - secondLen):
            maxFirst = max(maxFirst, prefix[i] - prefix[i - firstLen])
            res = max(res, maxFirst + prefix[i + secondLen] - prefix[i])
            
        return res