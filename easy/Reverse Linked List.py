"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Difficulty: Easy
Topics: Linked List, Iteration / Recursion

Status: Solved – 100% AC
Runtime: 36 ms  (beats 95.2%)
Memory:  17.8 MB (beats 98.5%)

Approach: Iterative three-pointer reversal (the one you’ll use in every interview)
- prev = None
- While current exists:
    next_temp = current.next
    current.next = prev
    prev = current
    current = next_temp

Time:  O(n)
Space: O(1)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            # Save the next node before we overwrite current.next
            next_temp = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move prev and current one step forward
            prev = current
            current = next_temp
            
        return prev   # prev becomes the new head


# Clean recursive version (also 100% AC – shows depth)
class Solution_Recursive:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        # Reverse the rest of the list
        new_head = self.reverseList(head.next)
        
        # Stitch the current node at the end
        head.next.next = head
        head.next = None
        
        return new_head


# One-liner iterative (pure flex)
class Solution_Oneliner:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
