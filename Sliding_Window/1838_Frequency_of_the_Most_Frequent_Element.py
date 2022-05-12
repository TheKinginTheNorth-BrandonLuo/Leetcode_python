# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:41:58 2022

@author: Fan Luo
"""
"""
1838. Frequency of the Most Frequent Element

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
"""
class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        l, r = 0, 0
        res, total = 0, 0
        while r < len(nums):
            total += nums[r]
            
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
                
            res = max(res, r - l + 1)
            r += 1
        
        return res