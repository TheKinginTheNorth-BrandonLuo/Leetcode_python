# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:34:10 2022

@author: Fan Luo
"""
"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""
class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if r == 0 and c == 0:
                    before = 0
                elif r == 0:
                    before = grid[r][c - 1]
                elif c == 0:
                    before = grid[r - 1][c]
                else:
                    before = min(grid[r - 1][c], grid[r][c - 1])
                grid[r][c] = before + grid[r][c]
                
        return grid[-1][-1]