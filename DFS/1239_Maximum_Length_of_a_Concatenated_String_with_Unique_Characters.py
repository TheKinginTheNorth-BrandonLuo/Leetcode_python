# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:46:34 2022

@author: Fan Luo
"""
"""
1239. Maximum Length of a Concatenated String with Unique Characters

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
"""
class Solution:
    def maxLength(self, arr):
        if not arr:
            return 0
        
        res = [0]
        
        def dfs(arr, sub_arr, idx):
            if len(sub_arr) != len(set(sub_arr)): # means there has duplicate
                return
            
            res[0] = max(res[0], len(sub_arr))
            
            for i in range(idx, len(arr)):
                dfs(arr, sub_arr + arr[i], i + 1)
         
        dfs(arr, "", 0)
        return res[0]