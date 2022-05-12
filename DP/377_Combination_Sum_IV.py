# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:28:10 2022

@author: Fan Luo
"""
"""
377. Combination Sum IV

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
"""
class Solution:
    def combinationSum4(self, nums, target):
        """
        example [1,2,3] target = 4
        0(initial dp[0]) -> 1
        1 -> 1
        2 -> 2 --1 + 1
        3 - > 4 --1 + 1 + 2
        4 -> 7 --4 + 2 + 1

        """
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for n in nums:
                if n <= i:
                    dp[i] += dp[i - n]
                    
        return dp[-1]