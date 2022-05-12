# -*- coding: utf-8 -*-
"""
Created on Mon May  2 20:04:12 2022

@author: Fan Luo
"""
"""
1094. Car Pooling

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
"""
class Solution:
    def carPooling(self, trips, capacity):
        res = [0] * 1001
        for t in trips:
            n, start, end = t
            res[start] += n
            res[end] -= n
            
        curPassenger = 0
        for i in range(1001):
            curPassenger += res[i]
            if curPassenger > capacity:
                return False
        return True
        