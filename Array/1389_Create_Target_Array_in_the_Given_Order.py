# -*- coding: utf-8 -*-
"""
Created on Sun May  8 15:49:43 2022

@author: Fan Luo
"""
"""
1389. Create Target Array in the Given Order

Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
"""
class Solution:
    def createTargetArray(self, nums, index):
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res
    
class Solution2:
    def createTargetArray(self, nums, index):
        res = []
        for i, n in zip(index, nums):
            # res[:i] + res[i] + res[i+1:]
            res[i:i] = [n]
        return res