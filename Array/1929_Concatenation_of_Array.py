# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 22:00:42 2022

@author: Fan Luo
"""
"""
1929. Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""
class Solution:
    def getConcatenation(self, nums):
        return nums + nums