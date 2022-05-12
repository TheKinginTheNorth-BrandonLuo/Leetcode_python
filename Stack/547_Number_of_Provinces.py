# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:27:34 2022

@author: Fan Luo
"""
"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""
class Solution:
    def findCircleNum(self, isConnected):
        # n = how many cities we have
        n = len(isConnected)
        res = 0
        visit = set()
        
        for i in range(n):
            if i in visit:
                continue
            # if ith city not visited, make it into stack
            s = [i]
            visit.add(i)
            res += 1
            while s:
                cur = s.pop()
                for j in range(n):
                    # if jth city not visited and its pos number is 1 which means it could connect
                    if j not in visit and isConnected[cur][j] == 1:
                        s.append(j)
                        visit.add(j)
        return res
    
    
"""
DFS version
"""
class Solution2:
    def findCircleNum(self, isConnected):
        visited = [0] * len(isConnected)
        count = 0
        for i in range(len(isConnected)):
            if visited[i] == 0:
                self.dfs(isConnected, visited, i)
                count += 1
                
        return count
        
    def dfs(self, isConnected, visited, i):
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(isConnected, visited, j)