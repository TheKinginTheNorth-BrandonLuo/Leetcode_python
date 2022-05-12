# -*- coding: utf-8 -*-
"""
Created on Sun May  1 13:37:19 2022

@author: Fan Luo
"""
"""
30. Substring with Concatenation of All Words

You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
"""
import collections

class Solution:
    def findSubstring(self, s, words):
        hash_map = collections.Counter(words)
        m = len(words)
        n = len(words[0])
        res = []
        
        for k in range(n):
            l = k
            subd = collections.defaultdict(int)
            count = 0
            for j in range(k, len(s) - n + 1, n):
                word = s[j: j + n]
                if word in hash_map:
                    subd[word] += 1
                    count += 1
                    while subd[word] > hash_map[word]:
                        subd[s[l: l + n]] -= 1
                        l += n
                        count -= 1
                    if count == m:
                        res.append(l)
                
                else:
                    l = j + n
                    subd = collections.defaultdict(int)
                    count = 0
                    
        return res