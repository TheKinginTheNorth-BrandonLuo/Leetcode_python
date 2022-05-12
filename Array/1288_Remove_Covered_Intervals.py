# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:47:31 2022

@author: Fan Luo
"""
"""
1288. Remove Covered Intervals

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), 
        remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
"""
class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x: (x[0], -x[1]))
        res = prev = 0
        for _, r in intervals:
            if r > prev:
                res += 1
                prev = r
                
        return res
        