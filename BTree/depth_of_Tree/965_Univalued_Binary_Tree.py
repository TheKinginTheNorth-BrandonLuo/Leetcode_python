# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 21:01:02 2022

@author: Fan Luo
"""
"""
965. Univalued Binary Tree

A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Input: root = [1,1,1,1,1,null,1]
Output: true
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class DFS_Solution:
    def isUnivalTree(self, root):
        def dfs(node, target):
            if not node:
                return True
            else:
                if node.val != target:
                    return False
            return dfs(node.left, target) and dfs(node.right, target)
        
        return dfs(root, root.val)
    
class Recursive_Solution:
    def isUnivalTree(self, root):
        if root == None:
            return True
        if root.left and root.left != root.val:
            return False
        if root.right and root.right != root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)