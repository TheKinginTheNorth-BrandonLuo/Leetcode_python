# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:54:17 2022

@author: Fan Luo
"""
"""
441. Arranging Coins

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
"""
class Solution:
    def arrangeCoins(self, n):
        left, right = 1, n
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            mid_sum = (1 + mid) * mid / 2
            if mid_sum > n:
                right = mid - 1
            else:
                left = mid + 1
                res = max(mid, res)
        return res