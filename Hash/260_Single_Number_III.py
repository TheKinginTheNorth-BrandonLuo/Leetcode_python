# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:26:54 2022

@author: Fan Luo
"""
"""
260. Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
"""
class Solution:
    def singleNumber(self, nums):
        hash_set = set()
        for n in nums:
            if n in hash_set:
                hash_set.remove(n)
            else:
                hash_set.add(n)
                
        return hash_set