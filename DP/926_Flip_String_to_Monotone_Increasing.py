# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:25:01 2022

@author: Fan Luo
"""
"""
926. Flip String to Monotone Increasing

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
"""
class Solution:
    def minFlipsMonoIncr(self, s):
        zero, one = s.count("0"), 0
        res = zero
        for c in s:
            if c == "0":
                zero -= 1
            else:
                one += 1
            res = min(res, zero + one)
        return res