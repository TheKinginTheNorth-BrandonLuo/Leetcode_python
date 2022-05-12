# -*- coding: utf-8 -*-
"""
Created on Sun May  1 16:56:26 2022

@author: Fan Luo
"""
"""
526. Beautiful Arrangement

Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
"""
class Solution:
    def countArrangement(self, n):
        def backtrack(n, pos, visited):
            if pos > n:
                res[0] += 1
            for i in range(1, n + 1):
                if not visited[i] and (pos % i == 0 or i % pos == 0):
                    visited[i] = True
                    backtrack(n, pos + 1, visited)
                    # finish first round searching
                    # set back to default
                    visited[i] = False
        
        res = [0]
        visited = [False] * (n+1) 
        backtrack(n, 1, visited)
        return res[0]