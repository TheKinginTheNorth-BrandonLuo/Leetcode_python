# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:51:42 2022

@author: Fan Luo
"""
"""
365. Water and Jug Problem

You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example 
"""

class Solution:
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        return targetCapacity == 0 or (jug1Capacity + jug2Capacity >= targetCapacity and targetCapacity % self.gcd(jug1Capacity, jug2Capacity) == 0)
        
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)
    
    
if __name__ == '__main__':
    jug1Capacity = 3
    jug2Capacity = 5
    targetCapacity = 4
    print(Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))