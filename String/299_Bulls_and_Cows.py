# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:02:56 2022

@author: Fan Luo
"""
"""
299. Bulls and Cows

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. 
When your friend makes a guess, you provide a hint with the following info:

1. The number of "bulls", which are digits in the guess that are in the correct position.
2. The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
3. Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
Note that both secret and guess may contain duplicate digits.

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
"""
import collections

class Solution:
    def getHint(self, secret, guess):
        bull, cow = 0, 0
        s = list(secret)
        g = list(guess)
        
        i, j = 0, 0
        while i < len(secret):
            if s[j] == g[j]:
                bull += 1
                s.pop(j)
                g.pop(j)
            else:
                j += 1
            i += 1
            
        count = collections.Counter(s)
        
        for letter in g:
            if letter in count and count[letter] > 0:
                cow += 1
                count[letter] -= 1
                
        return "{}A{}B".format(bull, cow)