# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:19:43 2022

@author: Fan Luo
"""
"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""
class Solution:
    def findDisappearedNumbers(self, nums):
        for n in nums:
            index = abs(n) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]