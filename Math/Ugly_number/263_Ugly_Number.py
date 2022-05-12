# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:23:49 2022

@author: Fan Luo
"""
"""
263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
"""
class Solution:
    def isUgly(self, n):
        if n == 0:
            return False
        
        for f in [2, 3, 5]:
            while n % f == 0:
                n /= f
            if n == 1:
                return True
        return False