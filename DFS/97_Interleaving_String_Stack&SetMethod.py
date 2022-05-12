# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:55:34 2022

@author: Fan Luo
"""
"""
97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
"""
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        visited = set((0, 0))
        stack = [(0, 0)]
        
        while stack:
            i, j = stack.pop()
            if i + j == len(s3):
                return True
            if i + 1 <= len(s1) and s1[i] == s3[i + j] and (i + 1, j) not in visited:
                stack.append((i + 1, j))
                visited.add((i + 1, j))
            if j + 1 <= len(s2) and s2[j] == s3[i + j] and (i, j + 1) not in visited:
                stack.append((i, j + 1))
                visited.add((i, j + 1))
        
        return False