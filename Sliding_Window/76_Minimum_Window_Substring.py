# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 09:47:30 2022

@author: Fan Luo
"""
"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""
import collections

class Solution:
    def minWindow(self, s, t):
        hash_map = collections.Counter(t)
        missing = len(t)
        start, end = 0, 0
        min_window = ""
        
        for end in range(len(s)):
            if hash_map[s[end]] > 0:
                missing -= 1
            hash_map[s[end]] -= 1
            
            while missing == 0:
                windowLength = end - start + 1
                if not min_window or windowLength < len(min_window):
                    min_window = s[start: end + 1]
                    
                hash_map[s[start]] += 1
                if hash_map[s[start]] > 0:
                    missing += 1
                
                start += 1
                
        return min_window