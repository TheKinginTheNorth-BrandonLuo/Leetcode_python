# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:17:17 2022

@author: Fan Luo
"""
"""
1528. Shuffle String

You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
"""
class Solution:
    def restoreString(self, s, indices):
        res = [""] * len(s)
        for i, c in zip(indices, s):
            res[i] = c  
            
        return "".join(res)
    
        #res = [""] * len(s)
        #for i, c in enumerate(s):
            #res[indices[i]] = c  
            
        #return "".join(res)