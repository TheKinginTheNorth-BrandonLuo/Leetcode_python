# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:08:57 2022

@author: Fan Luo
"""
"""
1898. Maximum Number of Removable Characters

You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

Return the maximum k you can choose such that p is still a subsequence of s after the removals.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

Input: s = "abcacb", p = "ab", removable = [3,1,0]
Output: 2
Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
"ab" is a subsequence of "accb".
If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
Hence, the maximum k is 2.
"""
class Solution:
    def maximumRemovals(self, s, p, removable):
        def isSubseq(s, subseq):
            i, j = 0, 0
            while i < len(s) and j < len(subseq):
                if i in removed or s[i] != subseq[j]:
                    i += 1
                    continue
                i += 1
                j += 1
                
            return j == len(subseq)
       
        res = 0
        l, r = 0, len(removable) - 1
        while l <= r:
            m = (l + r) // 2
            removed = set(removable[:m + 1])
            if isSubseq(s, p):
                res = max(res, m + 1)
                l = m + 1
            else:
                r = m - 1
                
        return res