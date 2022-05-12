# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:22:22 2022

@author: Fan Luo
"""
"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Input: nums = [3,2,3]
Output: [3]
"""
class Solution:
    def majorityElement(self, nums):
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        res = []
        for i in dic:
            if dic[i] > (len(nums) // 3):
                res.append(i)
        return res

