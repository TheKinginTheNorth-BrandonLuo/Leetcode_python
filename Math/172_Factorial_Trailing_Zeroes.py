# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 09:44:06 2022

@author: Fan Luo
"""
"""
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
"""
class Solution:
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        
        r = 0
        while n > 0:
            n = n // 5
            r += n
            
        return r