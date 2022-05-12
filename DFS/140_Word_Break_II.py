# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:58:56 2022

@author: Fan Luo
"""
"""
140. Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
"""
class Solution:
    def wordBreak(self, s, wordDict):
        memo = {}
        word_set = set(wordDict)
        return self.dfs(s, word_set, memo)
        
    def dfs(self, s, word_set, memo):
        if s in memo:
            return memo[s]
        if not s:
            return [""]
        res = []
        for i in range(1, len(s) + 1):
            if s[:i] in word_set:
                for word in self.dfs(s[i:], word_set, memo):
                    res.append(s[:i] + (" " if word else "") + word)
        memo[s] = res
        return res