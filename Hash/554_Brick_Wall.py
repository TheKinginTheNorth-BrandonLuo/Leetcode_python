# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:08:08 2022

@author: Fan Luo
"""
"""
554. Brick Wall

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2
"""
class Solution:
    def leastBricks(self, wall):
        count = {0:0} # count brick gaps
        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                count[total] = count.get(total, 0) + 1
                
        return len(wall) - max(count.values())