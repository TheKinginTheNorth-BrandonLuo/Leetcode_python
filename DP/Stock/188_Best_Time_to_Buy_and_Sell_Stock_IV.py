# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:33:02 2022

@author: Fan Luo
"""
"""
188. Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
"""
class Solution:
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0
        
        buy = [float("inf")] * k
        profits = [0] * k
        
        for p in prices:
            buy[0] = min(buy[0], p)
            profits[0] = max(profits[0], p - buy[0])
            for i in range(1, k):
                buy[i] = min(buy[i], p - profits[i - 1])
                profits[i] = max(profits[i], p - buy[i])
        
        return profits[-1]