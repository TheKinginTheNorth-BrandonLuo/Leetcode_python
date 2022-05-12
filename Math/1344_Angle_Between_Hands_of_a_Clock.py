# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:54:19 2022

@author: Fan Luo
"""
"""
1344. Angle Between Hands of a Clock

Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

Input: hour = 12, minutes = 30
Output: 165
"""
class Solution:
    def angleClock(self, hour, minutes):
        hour_hand = 30 * hour + 0.5 * minutes
        minute_hand = 6 * minutes
        diff = abs(hour_hand - minute_hand)
        return diff if diff <= 180 else 360 - diff