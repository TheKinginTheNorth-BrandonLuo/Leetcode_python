# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:26:11 2022

@author: Fan Luo
"""
"""
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""

""" 
1. for this question, we need to sort list first, for example, [8,1,2,2,3] becomes [1,2,2,3,8]
2. We use a hashmap to store the first show-up element indices in sorted list -> 1:0, 2:1, 3:3, 8: 4
3. The values of keys in hashmap indicate how many smaller values before current one
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        dic = {}
        res = []
        
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dic:
                dic[sorted_nums[i]] = i
        
        for i in range(len(nums)):
            res.append(dic[nums[i]])
            
        return res