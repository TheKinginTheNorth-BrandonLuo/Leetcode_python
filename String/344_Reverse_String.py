# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:30:32 2022

@author: Fan Luo
"""
"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1