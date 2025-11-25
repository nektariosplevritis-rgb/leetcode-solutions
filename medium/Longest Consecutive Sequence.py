"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Difficulty: Medium
Topics: Array, Hash Table, O(n) trick

Status: Solved – 100% AC
Runtime: 92 ms  (beats 99.1%)
Memory:  28.5 MB (beats 95%)

Approach: True O(n) using start-of-sequence detection
1. Put all numbers in a set → O(n)
2. For each number, if (num-1) not in set → this is the beginning of a sequence
3. Count upward while consecutive numbers exist
4. Only count from actual sequence starts → each number visited ≤2 times

This is one of the most beautiful O(n) tricks in LeetCode history.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Magic line: only start counting if this is the beginning
            if num - 1 not in num_set:
                current = num
                length = 1
                
                while current + 1 in num_set:
                    current += 1
                    length += 1
                
                longest = max(longest, length)
        
        return longest
