# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:21:49 2022

@author: Fan Luo
"""
"""
1380. Lucky Numbers in a Matrix

Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
"""
class Solution:
    def luckyNumbers (self, matrix):
        row_min = {min(row) for row in matrix}
        col_max = {max(col) for col in zip(*matrix)}
        
        return list(row_min & col_max)
    
matrix = [[3,7,8],[9,11,13],[15,16,17]]
if __name__ == '__main__':
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    print(Solution().luckyNumbers(matrix))