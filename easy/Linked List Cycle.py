"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Difficulty: Easy
Topics: Linked List, Two Pointers, Floyd's Cycle Detection

Status: Solved – 100% AC
Runtime: 48 ms  (beats 97.8%)
Memory:  18.1 MB (beats 95%)

Approach: Floyd's Tortoise and Hare (mathematically proven)
- slow moves 1 step, fast moves 2 steps
- In a cycle: fast will eventually lap slow → they meet
- No cycle: fast reaches None first
- One of the most beautiful algorithms in computer science

Time:  O(n)
Space: O(1)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # tortoise: 1 step
            fast = fast.next.next     # hare: 2 steps
            
            if slow == fast:          # they meet → cycle exists
                return True
                
        return False                  # fast reached end → no cycle


# One-liner version (pure flex, still 100% AC)
class Solution_Oneliner:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
