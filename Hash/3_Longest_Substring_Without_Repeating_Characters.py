# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:45:42 2022

@author: Fan Luo
"""
"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left, right = 0, 0
        chars = set()
        res = 0
        while left < len(s) and right < len(s):
            if s[right] in chars:
                if s[left] in chars:
                    chars.remove(s[left])
                    left += 1
            else:
                chars.add(s[right])
                right += 1
                res = max(res, len(chars))
        return res