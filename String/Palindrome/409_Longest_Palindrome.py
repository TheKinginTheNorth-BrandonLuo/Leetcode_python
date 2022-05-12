# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:00:59 2022

@author: Fan Luo
"""
"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
import collections

class Solution:
    def longestPalindrome(self, s):
        odds = sum([freq % 2 for _, freq in collections.Counter(s).items()])
        return len(s) if odds <= 1 else len(s) - odds + 1
    
class Solution2:
    def longestPalindrome(self, s):
        if not s or len(s) == 0:
            return 0
        
        hashSet = set()
        count = 0
        
        for i in range(len(s)):
            if s[i] in hashSet:
                hashSet.remove(s[i])
                count += 1
            else:
                hashSet.add(s[i])
                
        if hashSet:
            return count * 2 + 1
        
        return count * 2