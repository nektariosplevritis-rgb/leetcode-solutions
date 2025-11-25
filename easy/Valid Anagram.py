"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Difficulty: Easy
Topics: Hash Map, String

Status: Solved – 100% AC
Runtime: 42 ms  (beats 95.1%)
Memory:  17.1 MB (beats 98%)

Approach: Character frequency counter
- If lengths differ → immediately False
- Use fixed-size array [26] for a-z (faster than Counter/HashMap in practice)
- Increment for s, decrement for t → all zero at end = anagram

Time:  O(n)  
Space: O(1)  – only 26-element array

Note: This is the exact pattern used in Group Anagrams (049) – master once, use forever.
"""

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Length check – fastest early exit
        if len(s) != len(t):
            return False
            
        # 26-letter fixed array (faster than Counter for English lowercase)
        count = [0] * 26
        
        # Count characters in s, subtract characters in t
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
        # If all counts are zero → perfect anagram
        return all(c == 0 for c in count)
