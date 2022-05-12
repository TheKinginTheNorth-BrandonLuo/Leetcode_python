# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:50:24 2022

@author: Fan Luo
"""
"""
410. Split Array Largest Sum

Given an array nums which consists of non-negative integers and an integer m, 
    you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
class Solution:
    def splitArray(self, nums, m):
        left, right = max(nums), sum(nums)
        
        def count(mid):
            count = 1
            total = 0
            
            for n in nums:
                if total + n <= mid:
                    total += n
                else:
                    total = n
                    count += 1
            return count
        
        
        
        while left < right:
            mid = (left + right) // 2
            if count(mid) <= m:
                right = mid
            else:
                left = mid + 1
                
        return left