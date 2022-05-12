# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:15:20 2022

@author: Fan Luo
"""
"""
2028. Find Missing Observations

You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
"""
class Solution:
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        total = mean * (m + n)
        
        n_total = total - sum(rolls)
        
        if n_total < n or n_total > n * 6:
            return []
        res = []
        while n_total:
            # since answer return any of them
            # we could take from max of it
            # imagine n_total = 14, n = 10. while we take 6, n_total = 8, n = 9
            # we can't let n > n_total
            # so maximum we could take is n_total - n + 1
            # however when n_total is 20, n is 10, the max we can take is 6
            dice = min(n_total - n + 1, 6)
            res.append(dice)
            n_total -= dice
            n -= 1
        
        return res