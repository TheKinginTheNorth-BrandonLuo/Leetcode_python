# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:47:14 2022

@author: Fan Luo
"""
"""
653. Two Sum IV - Input is a BST

Given the root of a Binary Search Tree and a target number k, 
    return true if there exist two elements in the BST such that their sum is equal to the given target.

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTarget(self, root, k):
        seen = set()
        def dfs(root, seen):
            if not root:
                return False
            c = k - root.val
            if c in seen:
                return True
            seen.add(root.val)
            return dfs(root.left, seen) or dfs(root.right, seen)
        return dfs(root, seen)