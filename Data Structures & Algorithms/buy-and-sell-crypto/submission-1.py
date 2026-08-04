class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        curr_prof = 0
        size = len(prices)
        left, right = 0, 1

        while left < right and right < size:
            if prices[right] <= prices[left]:
                left = right
                right += 1
                continue

            max_prof = max(max_prof, prices[right] - prices[left])
            right += 1

        return max_prof