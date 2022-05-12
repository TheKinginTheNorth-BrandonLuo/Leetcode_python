# -*- coding: utf-8 -*-
"""
Created on Sun May  1 13:48:16 2022

@author: Fan Luo
"""
"""
1335. Minimum Difficulty of a Job Schedule

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
"""
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if d > n:
            return -1
        dp = [[float("inf")] * (d + 1) for _ in range(n + 1)]
        
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for k in range(1, d + 1):
                maximum = 0
                for j in range(i - 1, k - 2, -1):
                    maximum = max(maximum, jobDifficulty[j])
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + maximum)
                    
         #[[0, inf, inf],
         #[inf, 6, inf],
         #[inf, 6, 11],
         #[inf, 6, 10],
         #[inf, 6, 9],
         #[inf, 6, 8],
         #[inf, 6, 7]]
        return dp[n][d]