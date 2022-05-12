# -*- coding: utf-8 -*-
"""
Created on Thu May  5 12:27:21 2022

@author: Fan Luo
"""
"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""
class Solution:
    def evalRPN(self, tokens):
        operatorMap = {
            "+": lambda l,r: l + r,
            "*": lambda l,r: l * r,
            "-": lambda l,r: l - r,
            "/": lambda l,r: int(l / r),
        }
        
        stack = []
        for token in tokens:
            if token in operatorMap:
                right = stack.pop()
                left = stack.pop()
                token = operatorMap[token](left, right)
            
            stack.append(int(token))
        
        return stack.pop()
    
    
class Solution2:
    def evalRPN(self, tokens):
        stack = []
        
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        
        return stack[0]