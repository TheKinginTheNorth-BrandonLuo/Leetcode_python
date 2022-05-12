# -*- coding: utf-8 -*-
"""
Created on Sun May  8 13:21:09 2022

@author: Fan Luo
"""
"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
"""
class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i : [] for i in range(numCourses)}
        for course, pre_course in prerequisites:
            preMap[course].append(pre_course)
        cycle = set()
        visit = set()
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True