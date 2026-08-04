class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for l in range(len(prices)):
            r=l
            while r < len(prices) and prices[r] >= prices[l]:
                max_profit = max(max_profit, prices[r]-prices[l])
                r += 1
        return max_profit