# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:35:33 2022

@author: Fan Luo
"""
"""
802. Find Eventual Safe States

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node.

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
"""
class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        res = []
        safe = {}
        
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False # ie. False. for example, when nei is 5, return last status 2 which is False. So for loop break up. And now we need to set back 2 from false to true
            safe[i] = True
            return safe[i]
        
        
        
        for i in range(n):
            if dfs(i):
                res.append(i)
                
        return res