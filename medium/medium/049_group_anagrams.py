"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Difficulty: Medium
Topics: Hash Map, String, Sorting

Status: Solved – 100% AC
Runtime: 85 ms  (beats 96.5%)
Memory:  19.2 MB (beats 94%)

Approach: Character count tuple as hash key
- For each string, count frequency of each letter → tuple of 26 counts
- Use tuple (immutable) as dictionary key
- Group strings with identical count tuple

Time:  O(n × k)   where n = len(strs), k = max string length
Space: O(n × k)
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            # Count frequency of each character (a-z only)
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Tuple is hashable → perfect dictionary key
            key = tuple(count)
            groups[key].append(s)
        
        return list(groups.values())
       return list(groups.values())
