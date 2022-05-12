# -*- coding: utf-8 -*-
"""
Created on Wed May  4 21:16:24 2022

@author: Fan Luo
"""
"""
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""
class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        sCount = {}
        pCount = {}
        
        for i in range(len(p)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            pCount[p[i]] = pCount.get(p[i], 0) + 1
        
        res = [0] if sCount == pCount else []
        l = 0
        
        for r in range(len(p), len(s)):
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            sCount[s[l]] -= 1
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
        
        return res