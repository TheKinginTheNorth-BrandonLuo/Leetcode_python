# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:21:56 2022

@author: Fan Luo
"""
"""
2001. Number of Pairs of Interchangeable Rectangles

You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

Return the number of pairs of interchangeable rectangles in rectangles.

Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
Output: 6
Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
- Rectangle 0 with rectangle 1: 4/8 == 3/6.
- Rectangle 0 with rectangle 2: 4/8 == 10/20.
- Rectangle 0 with rectangle 3: 4/8 == 15/30.
- Rectangle 1 with rectangle 2: 3/6 == 10/20.
- Rectangle 1 with rectangle 3: 3/6 == 15/30.
- Rectangle 2 with rectangle 3: 10/20 == 15/30.
"""
class Solution:
    def interchangeableRectangles(self, rectangles):
        count = {}
        for w, h in rectangles:
            count[w/h] = count.get(w/h, 0) + 1
            
        res = 0
        for c in count.values():
            if c > 1:
                res += (c * (c - 1)) // 2
                
        return res
            
