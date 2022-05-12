# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:16:54 2022

@author: Fan Luo
"""
"""
590. N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value (See examples)

Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
class Solution:
    def postorder(self, root):
        res = []
        
        def dfs(root):
            if not root:
                return
            
            
            for child in root.children:
                dfs(child)
            res.append(root.val)
            
        dfs(root)
        return res