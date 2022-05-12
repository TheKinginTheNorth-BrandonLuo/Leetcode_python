# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:29:06 2022

@author: Fan Luo
"""
"""
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
"""
class Solution:
    def numJewelsInStones(self, jewels, stones):
        setJ = set(jewels)
        
        return sum(s in setJ for s in stones)