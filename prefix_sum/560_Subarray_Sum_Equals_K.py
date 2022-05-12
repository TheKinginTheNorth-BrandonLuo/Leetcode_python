# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:43:56 2022

@author: Fan Luo
"""
"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Input: nums = [1,1,1], k = 2
Output: 2
"""
class Solution:
    def subarraySum(self, nums, k):
        res = 0
        prefixSum = 0
        hashMap = {0: 1}
        for n in nums:
            prefixSum += n
            if prefixSum - k in hashMap:
                res = res + hashMap[prefixSum - k]
            hashMap[prefixSum] = hashMap.get(prefixSum, 0) + 1
            
        return res