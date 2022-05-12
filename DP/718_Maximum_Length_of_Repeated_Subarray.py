# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:33:11 2022

@author: Fan Luo
"""
"""
718. Maximum Length of Repeated Subarray

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
"""
class Solution:
    def findLength(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        res = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                res = max(res, dp[i][j])
                
        return res