# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:05:34 2022

@author: Fan Luo
"""
"""
1963. Minimum Number of Swaps to Make the String Balanced

You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".
"""
class Solution:
    def minSwaps(self, s):
        close, maxClose = 0, 0
        
        for c in s:
            if c == "[":
                close -= 1
            else:
                close += 1
            # check max unbalance
            maxClose = max(maxClose, close)
            
        return (maxClose + 1) // 2