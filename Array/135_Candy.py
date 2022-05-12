# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:51:42 2022

@author: Fan Luo
"""
"""
135. Candy

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
"""
class Solution:
    def candy(self, ratings):
        n = len(ratings)
        res = [1] * n
        
        # straight traverse
        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                res[i + 1] = 1 + res[i]
                
        # reverse traverse
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                #[1,3,4,5,2] case
                res[i] = max(res[i],1 + res[i + 1])
                
        return sum(res)