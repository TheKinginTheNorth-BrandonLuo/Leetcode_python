# -*- coding: utf-8 -*-
"""
Created on Sun May  1 17:12:30 2022

@author: Fan Luo
"""
"""
682. Baseball Game

You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record. The test cases are generated so that the answer fits in a 32-bit integer.

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
"""
class Solution:
    def calPoints(self, ops):
        stack = []
        for c in ops:
            if c == "+":
                tmp1, tmp2 = stack[-1], stack[-2]
                stack.append(tmp1 + tmp2)
            elif c == "D":
                tmp = stack[-1]
                stack.append(tmp*2)
            elif c == "C":
                stack.pop()
            else:
                stack.append(int(c))
                
        return sum(stack)