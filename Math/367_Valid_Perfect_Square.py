# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:20:26 2022

@author: Fan Luo
"""
"""
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Input: num = 16
Output: true
"""
"""
Equation: if a is a perfect square, a = 1 + 3 + 5 + 7 + 9 +...
"""

class Solution:
    def isPerfectSquare(self, num):
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0