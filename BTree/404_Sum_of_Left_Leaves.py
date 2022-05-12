# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:26:23 2022

@author: Fan Luo
"""
"""
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root):
        self.res = 0
        def dfs(root):
            if root:
                if root.left and not root.left.left and not root.left.right:
                    self.res += root.left.val
                    
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.res