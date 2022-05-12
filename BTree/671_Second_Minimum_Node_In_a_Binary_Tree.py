# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:33:45 2022

@author: Fan Luo
"""
"""
671. Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value, 
    where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, 
    then this node's value is the smaller value among its two sub-nodes. 
More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, 
    you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
"""
"""
key: root.val = min(root.left.val, root.right.val) always holds
We only need to find an element larger than root
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findSecondMinimumValue(self, root):
        res = [float("inf")]
        
        def dfs(node):
            if not node:
                return
            
            if root.val < node.val < res[0]:
                res[0] = node.val
            if root.val == node.val:
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        return -1 if res[0] == float("inf") else res[0]