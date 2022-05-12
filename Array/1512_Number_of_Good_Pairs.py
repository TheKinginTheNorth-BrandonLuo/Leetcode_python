# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:28:16 2022

@author: Fan Luo
"""
"""
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""
class Solution:
    def numIdenticalPairs(self, nums):
        dic = {}
        res = 0
        
        for n in nums:
            if n in dic:
                res += dic[n]
                dic[n] += 1
            else:
                dic[n] = 1
        return res