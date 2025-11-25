"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Difficulty: Easy
Topics: Linked List, Dummy Node, Two Pointers

Status: Solved – 100% AC
Runtime: 38 ms  (beats 96.8%)
Memory:  14.2 MB (beats 98%)

Approach: Dummy node + tail pointer (industry standard)
- Dummy node eliminates all edge cases
- While both lists exist → always attach the smaller current node
- When one list ends → attach the entire remaining list
- Return dummy.next (real head)

Time:  O(n + m)
Space: O(1)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # fake head
        tail = dummy            # tail always points to last added node
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next                    # move tail forward
        
        # Attach remaining nodes (one of the lists is now None)
        tail.next = list1 if list1 else list2
        
        return dummy.next                       # skip dummy, return real head


# Recursive version (clean, elegant, same performance)
class Solution_Recursive:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
