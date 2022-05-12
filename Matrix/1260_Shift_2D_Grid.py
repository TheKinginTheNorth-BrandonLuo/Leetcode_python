# -*- coding: utf-8 -*-
"""
Created on Sun May  1 13:13:52 2022

@author: Fan Luo
"""
"""
1260. Shift 2D Grid

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
"""
class Solution:
    def shiftGrid(self, grid, k):
        ROWS, COLS = len(grid), len(grid[0])
        
        def posToOneDArray(r, c):
            return r * COLS + c
        def oneDArrayToPos(val):
            return [val // COLS, val % COLS]
        
        res = [[0] * COLS for _ in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                newVal = (posToOneDArray(r, c) + k) % (ROWS * COLS)
                new_r, new_c = oneDArrayToPos(newVal)
                res[new_r][new_c] = grid[r][c]
                
        return res