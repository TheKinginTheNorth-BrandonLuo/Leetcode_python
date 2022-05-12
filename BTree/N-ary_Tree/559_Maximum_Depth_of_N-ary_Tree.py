# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:23:38 2022

@author: Fan Luo
"""
"""
559. Maximum Depth of N-ary Tree

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal,
     each group of children is separated by the null value (See examples).

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return 1 + max((self.maxDepth(node) for node in root.children), default = 0)