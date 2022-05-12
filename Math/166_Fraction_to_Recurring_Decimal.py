# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:19:30 2022

@author: Fan Luo
"""
"""
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Input: numerator = 1, denominator = 2
Output: "0.5"
"""
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        res = ""
        if numerator / denominator < 0:
            res += "-"
            
        n = abs(numerator)
        d = abs(denominator)
        r = n % d
        res += str(n // d)
        res += "."
        
        rPos = {}
        curQuotient = []
        index = 0
        
        while r != 0:
            rPos[r] = index
            index += 1
            curQuotient.append(str(r * 10 // d))
            r = r * 10 % d
            if r in rPos:
                pos = rPos[r]
                curQuotient.insert(pos, "(")
                curQuotient.append(")")
                break
            
        return res + "".join(curQuotient)