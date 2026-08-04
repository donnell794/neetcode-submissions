class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = max(nums)
        curr_min, curr_max = 1, 1
        for i in range(len(nums)):
            if nums[i] == 0:
                curr_min, curr_max = 1, 1
                continue
            m = curr_min * nums[i]
            n = curr_max * nums[i]
            curr_min = min(m,n, nums[i])
            curr_max = max(m,n, nums[i])
            max_ = max(max_, curr_max)

        return max_ or 0