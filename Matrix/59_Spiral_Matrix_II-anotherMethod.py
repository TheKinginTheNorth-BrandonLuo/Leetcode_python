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
        
        if n == 0:
            return res
        
        rowBegin, rowEnd, colBegin, colEnd = 0, n - 1, 0, n - 1
        num = 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):
                res[rowBegin][i] = num
                num += 1
            rowBegin += 1

            for j in range(rowBegin, rowEnd + 1):
                res[j][colEnd] = num
                num += 1
            colEnd -= 1

            for i in range(colEnd, colBegin - 1, -1):
                res[rowEnd][i] = num
                num += 1
            rowEnd -= 1

            for j in range(rowEnd, rowBegin - 1, -1):
                res[j][colBegin] = num
                num += 1
            colBegin += 1

        return res
