# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:17:23 2022

@author: Fan Luo
"""
"""
1029. Two City Scheduling

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
"""
class Solution:
    def twoCitySchedCost(self, costs):
        diffs = []
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])
        
        res = 0
        diffs.sort()
        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]
                
        return res