# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:19:20 2022

@author: Fan Luo
"""
"""
472. Concatenated Words

Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
"""
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        words_set = set(words)
        memo = {}
        
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words_set and suffix in words_set:
                    memo[word] = True
                    break
                if prefix in words_set and dfs(suffix):
                    memo[word] = True
                    break
                if suffix in words_set and dfs(prefix):
                    memo[word] = True
                    break
            return memo[word]
        
        return [word for word in words if dfs(word)]