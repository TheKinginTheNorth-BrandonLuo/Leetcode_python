# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:01:51 2022

@author: Fan Luo
"""
"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""

class Solution:
    def sortedSquares(self, nums):
        left, right = 0, len(nums) - 1
        res = []
        
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        return res[::-1]