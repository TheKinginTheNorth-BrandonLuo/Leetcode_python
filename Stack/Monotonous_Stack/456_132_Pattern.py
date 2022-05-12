# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:07:11 2022

@author: Fan Luo
"""
"""
456. 132 Pattern

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] 
    such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
"""

class Solution:
    def find132pattern(self, nums):
        N = len(nums)
        stack, two = [], float("-inf")
        
        for i in range(N - 1, -1, -1):
            if nums[i] < two:
                return True
            while stack and stack[-1] < nums[i]:
                two = stack.pop()
            stack.append(nums[i])
        return False