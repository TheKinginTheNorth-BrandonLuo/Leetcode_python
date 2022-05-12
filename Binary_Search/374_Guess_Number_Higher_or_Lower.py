# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:03:14 2022

@author: Fan Luo
"""
"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

    -1: Your guess is higher than the number I picked (i.e. num > pick).
    1: Your guess is lower than the number I picked (i.e. num < pick).
    0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Input: n = 10, pick = 6
Output: 6
"""
    
class Solution:
    def guessNumber(self, n):
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high = mid - 1
            else:
                low = mid + 1