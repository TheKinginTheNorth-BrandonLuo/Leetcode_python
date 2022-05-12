# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:41:03 2022

@author: Fan Luo
"""
"""
204. Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i]:
                for j in range(i + i, n, i):
                    res[j] = False
                    
        return res.count(True)
    
    
class SecondSolution:
    def countPrimes2(self, n):
        if n < 2:
            return 0
        
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, int(n**0.5) + 1):
            if res[i]:
                res[i + i:n:i] = [False] * len(res[i + i:n:i])
                
        return sum(res)