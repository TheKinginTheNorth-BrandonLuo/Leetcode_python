# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 13:46:45 2022

@author: Fan Luo
"""
"""
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
"""
class Solution:
    def generateMatrix(self, n):
        res = [[0] * n for _ in range(n)]
        r, c, dr, dc = 0, 0, 1, 0
        
        for i in range(n * n):
            # when you traverse first row, you increase r + dr, 
            # it should be column since you traverse all columns in first row
            res[c][r] = i + 1
            if not 0 <= r + dr < n or not 0 <= c + dc < n or res[c + dc][r + dr] != 0:
                dr, dc = -dc, dr
            r, c = r + dr, c + dc
            
        return res