"""
217. Contains Duplicate
Difficulty: Easy
Solved: 23 Nov 2025

Time:  O(n)    → single pass
Space: O(n)    → worst case all unique

Insight:
Hash set gives O(1) lookup → detects duplicate instantly.
Brute force O(n²) fails on 10⁵ elements.

Edge cases:
[]          → False
[1]         → False
[1,1]       → True (early return)

Example: [1,2,5,1]
→ set: {1} → {1,2} → {1,2,5} → 1 already exists → return True
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
