# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:46:33 2022

@author: Fan Luo
"""
"""
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def allPossibleFBT(self, n):
        dp = {0: [], 1: [TreeNode()]}
        
        def dfs(n):
            if n in dp:
                return dp[n]
            
            res = []
            for left in range(n):
                right = n - 1 - left
                
                leftTree, rightTree = dfs(left), dfs(right)
                
                for l1 in leftTree:
                    for r1 in rightTree:
                        res.append(TreeNode(0, l1, r1))
                        
            dp[n] = res
            return res
        
        return dfs(n)