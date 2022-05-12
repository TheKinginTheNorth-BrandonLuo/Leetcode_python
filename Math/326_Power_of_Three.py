# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:38:26 2022

@author: Fan Luo
"""
"""
326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Input: n = 27
Output: true
"""
class Solution:
    def isPowerOfThree(self, n):
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n / 3)