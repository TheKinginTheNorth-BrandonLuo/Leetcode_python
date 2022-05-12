# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:12:26 2022

@author: Fan Luo
"""
"""
709. To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Input: s = "Hello"
Output: "hello"
"""
class Solution:
    def toLowerCase(self, s):
        return "".join((chr(ord(c) + 32) if 65 <= c <= 90 else c for c in s))