# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:57:19 2022

@author: Fan Luo
"""
"""
1022. Sum of Root To Leaf Binary Numbers

You are given the root of a binary tree where each node has a value 0 or 1. 
Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. 
Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root):
        res = [0]
        
        def dfs(root, res, path):
            if not root.left and not root.right:
                path += str(root.val)
                res[0] += int(path, 2)
                
            if root.left:
                dfs(root.left, res, path + str(root.val))
            if root.right:
                dfs(root.right, res, path + str(root.val))
                
        dfs(root, res, "")
        return res[0]