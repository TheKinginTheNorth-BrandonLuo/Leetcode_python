# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:49:41 2022

@author: Fan Luo
"""
"""
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
"""
class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        dic = {}
        for i in range(len(words)):
            if pattern[i] not in dic:
                if words[i] in dic.values(): # avoid case "abba" "dog dog dog dog"
                    return False
                dic[pattern[i]] = words[i]
            else:
                if dic[pattern[i]] != words[i]:
                    return False
                
        return True