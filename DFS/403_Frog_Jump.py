# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:53:39 2022

@author: Fan Luo
"""
"""
403. Frog Jump

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
"""
class Solution:
    def canCross(self, stones):
        target = stones[-1]
        memo = set()
        stones = set(stones)
        return self.dfs(stones, 1, 1, target, memo)
        
        
    def dfs(self, stones, pos, jump, target, memo):
        if (pos, jump) in memo:
            return False
        if pos == target:
            return True
        if jump <= 0 or pos not in stones:
            return False
        for j in (jump - 1, jump, jump + 1):
            if self.dfs(stones, pos + j, j, target, memo):
                return True
        memo.add((pos, jump))
        return False