# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:21:37 2022

@author: Fan Luo
"""
"""
669. Trim a Binary Search Tree

Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def trimBST(self, root, low, high):
        if not root:
            return None
        if low > root.val:
            return self.trimBST(root.right, low, high)
        elif high < root.val:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root