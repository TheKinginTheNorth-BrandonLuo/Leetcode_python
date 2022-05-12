# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 13:32:47 2022

@author: Fan Luo
"""
"""
168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
    
    A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Input: columnNumber = 28
Output: "AB"
"""
class Solution:
    def convertToTitle(self, columnNumber):
        res = ""
        
        while columnNumber:
            res += chr(ord("A") + (columnNumber - 1) % 26)
            columnNumber = (columnNumber - 1) // 26
            
        return res[::-1]