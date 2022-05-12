# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:53:25 2022

@author: Fan Luo
"""
"""
309. Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
class Solution:
    def maxProfit(self, prices):
#         hold -----do nothing----->hold

#         hold -----sell----->notHold_cooldown

#         notHold -----do nothing -----> notHold

#         notHold -----buy-----> hold

#         notHold_cooldown -----do nothing----->notHold
        hold, notHold, notHoldCoolDown = float('-inf'), 0, float('-inf')
        
        for p in prices:
            hold, notHold, notHoldCoolDown = max(hold, notHold - p), max(notHold, notHoldCoolDown), hold + p
            
        return max(notHold, notHoldCoolDown)