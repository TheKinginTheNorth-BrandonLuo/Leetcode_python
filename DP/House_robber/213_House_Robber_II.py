# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:53:14 2022

@author: Fan Luo
"""
"""
213. House Robber II

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, 
    and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
 return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
"""
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        
        if len(nums) <= 3:
            return max(nums)
        
        dp1, dp2 = 0, 0
        for n in nums[:-1]:
            tmp = dp1
            dp1 = max(n + dp2, dp1)
            dp2 = tmp
            
        dp3, dp4 = 0, 0
        for n in nums[1:]:
            tmp = dp3
            dp3 = max(n + dp4, dp3)
            dp4 = tmp
            
        return max(dp1, dp3)