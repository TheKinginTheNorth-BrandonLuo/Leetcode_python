# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:36:17 2022

@author: Fan Luo
"""
"""
538. Convert BST to Greater Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def convertBST(self, root):
        self.curSum = 0
        
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            tmp = node.val
            node.val += self.curSum
            self.curSum += tmp
            
            dfs(node.left)
            
        dfs(root)
        return root