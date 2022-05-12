# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:57:59 2022

@author: Fan Luo
"""
"""
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
"""
class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        def dfs(r, c, visited):
            if (r, c) in visited:
                return 
            visited.add((r, c))
            for x, y in directions:
                new_r, new_c = r + x, c + y
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, visited)
        
        for r in range(ROWS):
            # from first row to check if can traverse to atlantic
            dfs(r, 0, pacific)
            # from last row to check if can traverse to pacific
            dfs(r, COLS - 1, atlantic)
        
        
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)
            
        return list(pacific & atlantic)