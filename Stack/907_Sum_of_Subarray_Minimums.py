# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:48:54 2022

@author: Fan Luo
"""
"""
907. Sum of Subarray Minimums

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
"""
class Solution:
    def sumSubarrayMins(self, arr):
        # https://leetcode.com/problems/sum-of-subarray-minimums/discuss/257811/Python-O(n)-slightly-easier-to-grasp-solution-(explained)
        arr = [0] + arr
        res = [0] * len(arr)
        stack = [0]
        
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            res[i] = res[j] + (i - j) * (arr[i])
            stack.append(i)
            
        return sum(res) % (10 ** 9 + 7)