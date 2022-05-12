# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 20:52:52 2022

@author: Fan Luo
"""
"""
221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
"""
class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        
        for r in range(ROWS):
            dp[r][0] = int(matrix[r][0])
            
        for c in range(COLS):
            dp[0][c] = int(matrix[0][c])
            
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    
        return max(map(max, dp)) ** 2