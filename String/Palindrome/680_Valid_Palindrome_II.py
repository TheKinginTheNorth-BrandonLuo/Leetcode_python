# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:29:48 2022

@author: Fan Luo
"""
"""
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
"""
class Solution:
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1:r + 1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l += 1
            r -= 1
        return True