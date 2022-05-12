# -*- coding: utf-8 -*-
"""
Created on Sun May  8 13:24:18 2022

@author: Fan Luo
"""
"""
239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 """
import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        l, r = 0, 0
        res = []
        q = collections.deque()
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # when finish one window, left window moves to next, we need to pop off elements in q and start from 0
            if l > q[0]:
                q.popleft()
                
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        return res