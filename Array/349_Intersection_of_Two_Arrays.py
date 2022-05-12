# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:00:14 2022

@author: Fan Luo
"""
"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""
class Solution:
    def intersection(self, nums1, nums2):
        res = []
        for i in set(nums1):
            if i in set(nums2):
                res.append(i)
        return res
    
class SecondSolution:
    def intersection2(self, nums1, nums2):
        return list(set(nums1) & set(nums2))