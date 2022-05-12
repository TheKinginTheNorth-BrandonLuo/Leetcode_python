# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:30:57 2022

@author: Fan Luo
"""
"""
328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        
        oddCur = cur = head
        evenCur = evenHead = head.next
        
        i = 1
        
        while cur:
            if i > 2 and i % 2 != 0:
                oddCur.next = cur
                oddCur = oddCur.next
            elif i > 2 and i % 2 == 0:
                evenCur.next = cur
                evenCur = evenCur.next
            cur = cur.next
            i += 1
            
        oddCur.next = evenHead
        evenCur.next = None
        
        return head