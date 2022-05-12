# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:49:17 2022

@author: Fan Luo
"""
"""
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        
        # initialize first col
        for c in range(COLS):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1
            
        # initialize first row
        for r in range(ROWS):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1
            
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if obstacleGrid[r][c] == 1:
                    continue
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[-1][-1]