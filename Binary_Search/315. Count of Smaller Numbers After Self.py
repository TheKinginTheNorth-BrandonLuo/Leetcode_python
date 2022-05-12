# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:52:22 2022

@author: Fan Luo
"""
"""
315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""
from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums):
        s = SortedList()
        res = []
        
        for n in nums[::-1]:
            ans = SortedList.bisect_left(s, n)
            res.append(ans)
            s.add(n)
            
        return reversed(res)