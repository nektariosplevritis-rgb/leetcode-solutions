"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Difficulty: Medium
Topics: Two Pointers, Binary Search

Status: Solved – 100% AC
Runtime: 68 ms  (beats 98.9%)
Memory:  14.3 MB (beats 97%)

Approach: Two Pointers (optimal for sorted array)
- Left pointer at start, right at end
- Sum too big → move right left
- Sum too small → move left right
- Sum exact → return [left+1, right+1] (1-based index)

Time:  O(n)
Space: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]       # 1-based index as required
            elif current_sum < target:
                left += 1                         # need larger sum
            else:
                right -= 1                        # need smaller sum
                
        # Problem guarantees exactly one solution, so never reach here
        return [-1, -1]


# Alternative: Binary Search version (also valid, shows versatility)
class Solution_BinarySearch:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            complement = target - numbers[i]
            # Binary search in the remaining part (i+1 to end)
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    left = mid + 1
                else:
                    right = mid - 1
        return [-1, -1]
