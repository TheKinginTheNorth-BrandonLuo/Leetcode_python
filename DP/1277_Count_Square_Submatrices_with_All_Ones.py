# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:51:42 2022

@author: Fan Luo
"""
"""
1277. Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
"""
class Solution:
    def countSquares(self, matrix):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        count = 0
        
        for c in range(COLS):
            count += matrix[0][c]
        for r in range(1, ROWS):
            count += matrix[r][0]
            
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 1 and matrix[r - 1][c] > 0 and matrix[r][c - 1] > 0 and matrix[r - 1][c - 1] > 0:
                    matrix[r][c] += min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
                count += matrix[r][c]
                
        return count