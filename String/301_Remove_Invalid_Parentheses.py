# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:04:36 2022

@author: Fan Luo
"""
"""
301. Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Input: s = "()())()"
Output: ["(())()","()()()"]
"""
class Solution:
    def removeInvalidParentheses(self, s):
        level = {s}
        while level:
            res = []
            for p in level:
                if self.isValid(p):
                    res.append(p)
            if res:
                return res
            newLevel = set()
            for p in level:
                for i in range(len(p)):
                    newLevel.add(p[:i] + p[i + 1:])
            level = newLevel
                
        
    def isValid(self, s):
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0