# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:12:42 2022

@author: Fan Luo
"""
"""
897. Increasing Order Search Tree

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def increasingBST(self, root):
        def inOrder(root):
            if not root:
                return []
            return inOrder(root.left) + [root.val] + inOrder(root.right)
        
        res = inOrder(root)
        newRoot = cur = TreeNode(res[0])
        for i in range(1, len(res)):
            cur.right = TreeNode(res[i])
            cur = cur.right
            
        return newRoot