# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:15:37 2022

@author: Fan Luo
"""
"""
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""

import collections

class Solution:
    def intersect(self, nums1, nums2):
        res = []
        count = collections.Counter(nums1)
        
        for n in nums2:
            if n in count and count[n] > 0:
                res += [n]
                count[n] -= 1
        return res
    
if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution().intersect(nums1, nums2))