# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:54:34 2022

@author: Fan Luo
"""
"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Input: s = "abc", t = "ahbgdc"
Output: true
"""

class Solution:
    def isSubsequence(self, s, t):
        s = "!" + s
        t = "!" + t
        ROWS, COLS = len(t), len(s)
        dp = [[0] * COLS for _ in range(ROWS)]
        
        for r in range(ROWS):
            dp[r][0] = 1
            
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if t[r] == s[c]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = dp[r - 1][c]
                
        return dp[-1][-1] != 0
    
# Method 2: for loop
class Solution2:
    def isSubsequence(self, s, t):
        if not s:
            return True
        pos = 0
        for ch in t:
            if ch == s[pos]:
                pos += 1
                if pos == len(s):
                    return True
        return False
    
if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))