# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:50:58 2022

@author: Fan Luo
"""
"""
214. Shortest Palindrome

You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Input: s = "aacecaaa"
Output: "aaacecaaa"
"""
class Solution:
    def shortestPalindrome(self, s):
        if not s or len(s) == 1 or s == s[::-1]:
            return s
        r = s[::-1]
        n = len(s)
        
        for i in range(n - 1, -1, -1):
            if s[:i] == r[n - i:]:
                return r[:n - i] + s