# -*- coding: utf-8 -*-
"""
Created on Wed May  4 21:31:29 2022

@author: Fan Luo
"""
"""
343. Integer Break

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
"""
class Solution:
    def integerBreak(self, n):
        dp = [None, 1]
        for i in range(2, n + 1):
            r = i - 1
            l = 1
            max_product = 0
            while l <= r:
                max_product = max(max_product, max(l, dp[l]) * max(r, dp[r]))
                r -= 1
                l += 1
            dp.append(max_product)
            
        return dp[-1]