# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:44:51 2022

@author: Fan Luo
"""
"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""
import collections

class Solution:
    def checkInclusion(self, s1, s2):
        count = collections.Counter(s1)
        N = len(s1)
        res = 0
        
        for i in range(len(s2)):
            if s2[i] in count:
                count[s2[i]] -= 1
                if count[s2[i]] == 0:
                    res += 1
            if i >= N and s2[i - N] in count:
                if count[s2[i - N]] == 0:
                    res -= 1
                count[s2[i - N]] += 1
                    
            if res == len(count):
                return True
        return False