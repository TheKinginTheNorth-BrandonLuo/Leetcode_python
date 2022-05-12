# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:37:14 2022

@author: Fan Luo
"""
"""
1305. All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2, 
    return a list containing all the integers from both trees sorted in ascending order.

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1, root2):
        res1 = self.inOrder(root1)
        res2 = self.inOrder(root2)
        return sorted(res1 + res2)
        
    def inOrder(self, root):
        if not root:
            return []
        
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)