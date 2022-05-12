# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:58:41 2022

@author: Fan Luo
"""
"""
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        dummy = ListNode(0)
        
        while stack1 or stack2 or carry:
            add1 = stack1.pop() if stack1 else 0
            add2 = stack2.pop() if stack2 else 0
            tmp_sum = add1 + add2 + carry
            carry = 1 if tmp_sum >= 10 else 0
            tmp_sum = tmp_sum - 10 if tmp_sum >= 10 else tmp_sum
            cur = ListNode(tmp_sum)
            cur.next = dummy.next
            dummy.next = cur
            
        return dummy.next
            