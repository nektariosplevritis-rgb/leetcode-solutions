# 152. Maximum Product Subarray
Difficulty: Medium
Solved: 23 Nov 2025
Time: O(n)
Space: O(1)

Insight (one killer sentence):
→ Track both max and min product ending at each position because a negative can flip everything.

Edge cases handled:
→ All negatives → need the largest negative (or single element)
→ Zeros → reset both max and min

Example walk-through:
nums = [2,3,-2,4]
→ i=0: max_so_far=2, min_so_far=2
→ i=1: max_so_far=6, min_so_far=2
→ i=2: max_so_far=6, min_so_far=-12 (3*-2*2)
→ i=3: max_so_far=6, min_so_far=-48 → but new max = 4*-2 = -8 → wait, correct logic below

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min, cur_max = 1, 1
        
        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                continue
            tmp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            res = max(res, cur_max)
        return res
