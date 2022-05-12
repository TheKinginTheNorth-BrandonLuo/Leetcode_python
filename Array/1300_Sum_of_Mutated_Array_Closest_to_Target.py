# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:27:54 2022

@author: Fan Luo
"""
"""
1300. Sum of Mutated Array Closest to Target

Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
"""
class Solution:
    def findBestValue(self, arr, target):
        arr.sort()

        l = len(arr)

        for i in range(l):
            val = target / l
            sol = int(val) if val % 1 <= 0.5 else round(val)
            if arr[i] > sol:
                return sol
            else:
                target -= arr[i]
                l -= 1

        return arr[-1]