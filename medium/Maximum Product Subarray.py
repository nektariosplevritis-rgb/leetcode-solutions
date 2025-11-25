# 152. Maximum Product Subarray
# Difficulty: Medium
# Date Solved: 23 Nov 2025
# Time: O(n) | Space: O(1)

"""
Problem Summary
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest product and return the product.

Key Observations
- Negative numbers can invert the current minimum product to become the new maximum upon multiplication with another negative.
- Zeros interrupt the product chain and require resetting the running trackers.
- Tracking both maximum and minimum products at each step handles sign flips effectively.

Solution Approach
Use dynamic programming with two variables to maintain the running maximum and minimum products ending at the current index.
On encountering a negative number, swap the max and min trackers before updating to account for potential inversion.
Update the global result with the current maximum at each step.
This approach ensures optimal time and space complexity while covering all edge cases.
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Though LeetCode constraints ensure len(nums) >= 1
        
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # Temporarily store the current max for min calculation
            temp_max = max_prod
            
            # Update max and min considering the new number
            max_prod = max(num, max_prod * num, min_prod * num)
            min_prod = min(num, temp_max * num, min_prod * num)
            
            # Update the global result
            result = max(result, max_prod)
        
        return result
