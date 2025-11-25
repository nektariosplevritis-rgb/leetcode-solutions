"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Difficulty: Easy
Topics: Array, Dynamic Programming (Kadane-style)

Status: Solved – 100% AC
Runtime: 58 ms  (beats 99.2%)
Memory:  17.3 MB (beats 96%)

Approach: One-pass "lowest so far" tracking
- Keep track of the cheapest price seen up to now
- At each day, calculate profit if we sold today
- Update global max profit
- Classic "min-so-far" pattern – same idea as Maximum Subarray

Time:  O(n) – single pass
Space: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        min_price_so_far = prices[0]   # cheapest price we've seen
        max_profit = 0                 # best profit we could achieve
        
        for today_price in prices[1:]:
            # Option 1: do nothing, keep our current min_price
            # Option 2: maybe today is cheaper → update min_price
            min_price_so_far = min(min_price_so_far, today_price)
            
            # If we sold today (after possibly buying at min_price_so_far)
            profit_if_sold_today = today_price - min_price_so_far
            
            # Update our best possible profit
            max_profit = max(max_profit, profit_if_sold_today)
        
        return max_profit


# Alternative super-clean version (same speed)
class Solution_Clean:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
