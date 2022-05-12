# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 23:08:59 2022

@author: Fan Luo
"""
"""
137. Single Number II

Given an integer array nums where every element appears three times except for one, which appears exactly once. 
Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,3,2]
Output: 3
"""


class Solution:
    def singleNumber(self, nums):
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for i in dic:
            if dic[i] == 1:
                return i