# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:35:44 2022

@author: Fan Luo
"""
"""
904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
"""
class Solution:
    def totalFruit(self, fruits):
        res = 0
        hash_map = {}
        l, r = 0, 0
        
        while r < len(fruits):
            hash_map[fruits[r]] = r
            if len(hash_map) >= 3:
                minVal = min(hash_map.values())
                del hash_map[fruits[minVal]]
                l = minVal + 1
            res = max(res, r - l + 1)
            r += 1
            
        return res