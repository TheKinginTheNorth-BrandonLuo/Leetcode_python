# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:51:07 2022

@author: Fan Luo
"""
"""
513. Find Bottom Left Tree Value

Given the root of a binary tree, return the leftmost value in the last row of the tree.

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
"""

"""
Method 1: level order traversal and return first element in last list
"""
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return None
        
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            
        return node.val