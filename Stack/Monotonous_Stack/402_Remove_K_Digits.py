# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:45:49 2022

@author: Fan Luo
"""
"""
402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k, 
    return the smallest possible integer after removing k digits from num.

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
"""

class Solution:
    def removeKdigits(self, num: str, k):
        i, N = 0, len(num)
        
        stack = []
        if k >= N:
            return "0"
        
        while i < N:
            while stack and k > 0 and int(stack[-1]) > int(num[i]):
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        
        ## NOTE:there might be k still > 0 when case "112"
        ## since 112 has duplicate which not satisfy while stack and ....
        ## so not execute second while loop and only append
        ## Sp we need to pop one element
        while k > 0:
            stack.pop()
            k -= 1
        return str(int("".join(stack)))