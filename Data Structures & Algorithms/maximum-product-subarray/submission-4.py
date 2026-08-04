class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = max(nums)
        curr_min, curr_max = 1, 1
        for n in nums:
            if n == 0:
                curr_min, curr_max = 1, 1
                continue
            x = curr_min * n
            y = curr_max * n
            curr_min = min(x, y, n)
            curr_max = max(x, y, n)
            max_ = max(max_, curr_max)

        return max_