"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Difficulty: Easy
Topics: Two Pointers, String

Status: Solved – 100% AC
Runtime: 38 ms  (beats 97.8%)
Memory:  17.3 MB (beats 95%)

Approach: Two-pointer alphanumeric filter
- Ignore case + non-alphanumeric using built-in methods
- Left/right pointers → move inward until mismatch or done
- Pure Python one-liner filter version included

Time:  O(n)
Space: O(1)  – only pointers, no extra strings
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and keep only alphanumeric chars
        filtered = [c.lower() for c in s if c.isalnum()]
        
        # Two-pointer check
        left, right = 0, len(filtered) - 1
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        return True


# One-liner version (also 100% AC, recruiter eye-candy)
class Solution_Clean:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]


# Fastest pure two-pointer version (no list creation)
class Solution_Fastest:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True
