# -*- coding: utf-8 -*-
"""
Created on Thu May  5 13:58:17 2022

@author: Fan Luo
"""
"""
856. Score of Parentheses

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Input: s = "(())"
Output: 2
"""
class Solution:
    def scoreOfParentheses(self, s):
        stack = []
        
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                m = stack.pop()
                if m == "(":
                    stack.append(1)
                else: # stack has appended numbers
                    tmp = 0
                    while m != "(":
                        tmp += m
                        m = stack.pop()
                    stack.append(2 * tmp)
        return sum(stack)