# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:54:02 2022

@author: Fan Luo
"""
"""
1669. Merge In Between Linked Lists

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:
    
Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. 
The blue edges and nodes in the above figure indicate the result.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        head = list1
        for i in range(a - 1):
            head = head.next
            
        cur = head.next
        for i in range(b - a):
            cur = cur.next
            
        head.next = list2
        while head.next:
            head = head.next
            
        if cur.next:
            head.next = cur.next
            
        return list1