# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:13:21 2022

@author: Fan Luo
"""
"""
1110. Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
"""
class Solution:
    def delNodes(self, root, to_delete):
        def dfs(node, res):
            if node:
                dfs(node.left, res)
                dfs(node.right, res)
                if node.left and node.left.val in to_delete:
                    node.left = None
                if node.right and node.right.val in to_delete:
                    node.right = None
                if node.val in to_delete:
                    if node.left:
                        res.append(node.left)
                    if node.right:
                        res.append(node.right)
                        
        to_delete = set(to_delete)
        if not root:
            return []
        self.res = [] if root.val in to_delete else [root]
        dfs(root, self.res)
        return self.res