# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 20:44:33 2022

@author: Fan Luo
"""
"""
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        res = 0
        
        for n in nums:
            if n == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0
                
        return res