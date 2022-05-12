# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:21:38 2022

@author: Fan Luo
"""
"""
264. Ugly Number II

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
"""
class Solution:
    def nthUglyNumber(self, n):
        # Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5)
        two = three = five = 0
        ugly = [1]
        while len(ugly) < n:
            while ugly[two] * 2 <= ugly[-1]:
                two += 1
            while ugly[three] * 3 <= ugly[-1]:
                three += 1
            while ugly[five] * 5 <= ugly[-1]:
                five += 1
                
            ugly.append(min(ugly[two] * 2, ugly[three] * 3, ugly[five] * 5))
            
        return ugly[-1]