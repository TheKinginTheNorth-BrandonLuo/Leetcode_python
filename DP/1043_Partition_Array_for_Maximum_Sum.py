# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:43:02 2022

@author: Fan Luo
"""
"""
1043. Partition Array for Maximum Sum

Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
"""
class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        dp = [0 for _ in range(len(arr))]
        dp[0] = arr[0]
        max_first_k = arr[0]
        
        # initialize first k in dp array
        for i in range(1, k):
            max_first_k = max(max_first_k, arr[i])
            dp[i] = max_first_k*(i + 1)
        
        # for first example, dp = [0, 30, 45, 0, 0, 0, 0]
        # each index record largest sum before now
        # we start from index 3. We still need to partition to see arr[3] whether the largest of this interval not just using previous sum 45 and start count from begining
        for i in range(k, len(dp)):
            partition_max = 0
            for j in range(k):
                partition_max = max(partition_max, arr[i - j])
                prev_sum = dp[i - j - 1]
                dp[i] = max(dp[i], prev_sum + (j + 1) * partition_max)
               
        return dp[-1]
    
if __name__ == '__main__':
    arr = [1,4,1,5,7,3,6,1,9,9,3]
    k = 4
    
    print(Solution().maxSumAfterPartitioning(arr, k))