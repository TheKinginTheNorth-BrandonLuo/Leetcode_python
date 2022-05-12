# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:39:16 2022

@author: Fan Luo
"""
"""
322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""
class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
            
        return -1 if dp[-1] == float('inf') else dp[-1]