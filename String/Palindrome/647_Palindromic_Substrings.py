# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:17:21 2022

@author: Fan Luo
"""
"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
"""
class Solution:
    def countSubstrings(self, s):
        res = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            res += self.countPalin(s, i, i)
            res += self.countPalin(s, i, i + 1)
            
        return res
    
    def countPalin(self, s, l, r):
        res = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res