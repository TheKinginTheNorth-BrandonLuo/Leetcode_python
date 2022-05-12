# -*- coding: utf-8 -*-
"""
Created on Sun May  8 10:39:24 2022

@author: Fan Luo
"""
"""
337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root):
        def dfs(root):
            if not root:
                return [0, 0]
            
            leftPairs = dfs(root.left)
            rightPairs = dfs(root.right)
            
            robCurRoot = root.val + leftPairs[1] + rightPairs[1]
            skipCurRoot = max(leftPairs) + max(rightPairs)
            
            return [robCurRoot, skipCurRoot]
        
        return max(dfs(root))