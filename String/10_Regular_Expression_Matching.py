# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:40:11 2022

@author: Fan Luo
"""
"""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
"""
class Solution:
    def isMatch(self, s, p):
        if not p: return not s
        if not s: return len(p) > 1 and p[1] == '*' and self.isMatch(s, p[2:])
        Matched = (p[0] == '.' or p[0] == s[0])
        if len(p) > 1 and p[1] == '*':
            return (Matched and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        return Matched and self.isMatch(s[1:], p[1:])