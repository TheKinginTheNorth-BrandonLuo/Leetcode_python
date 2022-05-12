# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:25:27 2022

@author: Fan Luo
"""
"""
149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Input: points = [[1,1],[2,2],[3,3]]
Output: 3
"""
class Solution:
    def maxPoints(self, points):
        def helper(curPoint, points):
            k, duplicates, ans = {}, 0, 0
            x1, y1 = curPoint
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                else:
                    slope = (x2 - x1) / (y2 - y1) if y1 != y2 else "inf"
                    count = k.get(slope, 0) + 1
                    k[slope] = count
                    ans = max(ans, count)
                    
            return ans + duplicates + 1
        
        res = 0
        while points:
            curPoint = points.pop()
            res = max(res, helper(curPoint, points))
            
        return res