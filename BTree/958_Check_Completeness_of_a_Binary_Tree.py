'''
958. Check Completeness of a Binary Tree

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), 
and all nodes in the last level ({4, 5, 6}) are as far left as possible.
'''

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root):
        q = [root]
        missing = False
        while q:
            size = len(q)
            while size > 0:
                node = q.pop(0)
                size -= 1
                if node is None:
                    missing = True
                else:
                    # if there exists a node after a missing node
                    if missing:
                        return False
                    q.append(node.left)
                    q.append(node.right)
                    
        return True

class Solution2:
    def isCompleteTree(self, root):
        queue = collections.deque([root])
        hasNone = False
        
        while queue:
            node = queue.popleft()
            if not node:
                hasNone = True
            else:
                if hasNone:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True