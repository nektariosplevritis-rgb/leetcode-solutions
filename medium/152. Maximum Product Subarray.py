# 152. Maximum Product Subarray
Difficulty: Medium
Solved: 23 Nov 2025
Time: O(n)
Space: O(1)

Insight (one killer sentence):
→ Keep running max and min products because negatives flip losers into winners, so you can't drop the lows.

Edge cases handled:
→ All negatives: grabs the largest (least negative) product by tracking mins
→ Zeros: resets trackers without killing the global max
→ Single element: initializes and returns directly
→ Mix of positives/negatives/zeros: handles flips via min/max updates

Example walk-through:
nums = [2,3,-2,4]
→ res = 2, cur_max=2, cur_min=2
→ n=3: candidates max(3, 2*3=6, 2*3=6) → cur_max=6; min(3,2*3=6,2*3=6) → cur_min=3; res=6
→ n=-2: candidates max(-2, 6*-2=-12, 3*-2=-6) → cur_max=-2; min(-2,6*-2=-12,3*-2=-6) → cur_min=-12; res=6 (no change)
→ n=4: candidates max(4, -2*4=-8, -12*4=-48) → cur_max=4; min(4,-2*4=-8,-12*4=-48) → cur_min=-48; res=6
Output: 6 (from 2*3)

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge: empty, but LC guarantees >=1
        
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        
        for n in nums[1:]:
            # Candidates for new max/min: standalone n, or extend from prev max/min
            cand_max = max(n, cur_max * n, cur_min * n)
            cand_min = min(n, cur_max * n, cur_min * n)
            
            cur_max = cand_max
            cur_min = cand_min
            
            # Zero reset happens implicitly if n=0 (cand_max/cand_min=0)
            res = max(res, cur_max)
        
        return res
