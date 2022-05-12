# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:24:53 2022

@author: Fan Luo
"""
"""
395. Longest Substring with At Least K Repeating Characters

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
"""
class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
    
class Solution2:
    def longestSubstring(self, s, k):
        n = len(s)
        if n ==0 or n < k:
            return 0
        if k == 1:
            return n
        
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        target_char = '0'
        for i in range(26):
            if count[i] > 0 and count[i] < k:
                target_char = chr(i + ord('a'))
                break
                
        if target_char == '0':
            return n
        
        subs = s.split(target_char)
        res = 0
        for sub in subs:
            res = max(res, self.longestSubstring(sub, k))
            
        return res