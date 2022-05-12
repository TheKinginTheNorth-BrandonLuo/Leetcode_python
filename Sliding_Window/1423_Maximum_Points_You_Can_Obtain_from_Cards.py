# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:08:00 2022

@author: Fan Luo
"""
"""
1423. Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
"""
class Solution:
    def maxScore(self, cardPoints, k):
        sum_k = sum(cardPoints[:k])
        res = sum_k
        
        for i in range(1, k + 1):
            sum_k += cardPoints[-i] - cardPoints[k - i]
            res = max(res, sum_k)
            
        return res
    
if __name__ == '__main__':
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    print(Solution().maxScore(cardPoints, k))