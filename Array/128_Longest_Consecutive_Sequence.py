# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:31:01 2022

@author: Fan Luo
"""
"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution:
    def longestConsecutive(self, nums):
        res = 0
        nums = set(nums)
        
        for n in nums:
            if n - 1 not in nums:
                start = n
                while start in nums:
                    start += 1
                res = max(res, start - n)
        
        return res