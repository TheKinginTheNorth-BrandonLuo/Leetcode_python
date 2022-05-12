# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 13:57:48 2022

@author: Fan Luo
"""
"""
399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
"""
import collections

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(dict)
        N = len(equations)

        for i in range(N):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1/values[i]
            
        # visited = set()
        
        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1
            if y in graph[x]:
                return graph[x][y]
            
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    tmp = dfs(i, y, visited) # tmp = b/c=3
                    if tmp == -1: 
                        continue
                    else:
                        return tmp * graph[x][i] # tmp * b
            return -1
        
        res = []
        for x, y in queries:
            res.append(dfs(x, y, set()))
            
        return res