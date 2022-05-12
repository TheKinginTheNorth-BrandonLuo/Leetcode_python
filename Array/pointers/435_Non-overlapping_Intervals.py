# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:00:49 2022

@author: Fan Luo
"""
"""
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals):
        res = 0
        intervals.sort()
        prevEnd = intervals[0][1]
        
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
                
        return res