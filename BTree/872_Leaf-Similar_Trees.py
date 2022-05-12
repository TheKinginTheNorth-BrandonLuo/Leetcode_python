# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 20:37:51 2022

@author: Fan Luo
"""
"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1, root2):
        return self.dfs(root1) == self.dfs(root2)
    
    def dfs(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.dfs(root.left) + self.dfs(root.right)