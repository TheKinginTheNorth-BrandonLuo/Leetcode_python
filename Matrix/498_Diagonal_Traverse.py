# -*- coding: utf-8 -*-
"""
Created on Mon May  2 12:33:03 2022

@author: Fan Luo
"""
"""
498. Diagonal Traverse

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
"""
import collections

class Solution:
    def findDiagonalOrder(self, mat):
        ROWS, COLS = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for r in range(ROWS):
            for c in range(COLS):
                d[r + c].append(mat[r][c])
        
        res = []
        for item in d.items():
            if item[0] % 2 == 0:
                res += item[1][::-1]
            else:
                res += item[1]
                
        return res