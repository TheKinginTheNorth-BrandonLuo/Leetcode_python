# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 23:20:09 2022

@author: Fan Luo
"""
"""
115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
"""

class Solution:
    def numDistinct(self, s, t):
        dp = [([0] * (len(s) + 1)) for _ in range(len(t) + 1)]
        
        for _ in range((len(s) + 1)):
            dp[0][_] = 1
            
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
                    
        return dp[-1][-1]