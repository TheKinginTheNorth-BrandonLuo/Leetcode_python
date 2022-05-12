# -*- coding: utf-8 -*-
"""
Created on Thu May  5 20:58:54 2022

@author: Fan Luo
"""
"""
946. Validate Stack Sequences

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
"""
class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        N = len(popped)
        i = 0
        for p in pushed:
            stack.append(p)
            while stack and i < N and stack[-1] == popped[i]:
                i += 1
                stack.pop()
                
        return stack == []