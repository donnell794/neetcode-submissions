class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_profit = 0
        ln = len(prices)-1
        for l in range(ln):
            r = l + 1
            while r <= ln and prices[r] >= prices[l]:
                curr_profit = max(curr_profit, prices[r]-prices[l])
                r += 1
            max_profit = max(max_profit, curr_profit)
            
        return max_profit