class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(
            self.helper(nums[1:]),
            self.helper(nums[:-1])
        )

    def helper(self, nums):
        if len(nums) == 1:
            return nums[0]

        cache = [0] * len(nums)
        cache[0], cache[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cache[i] = max(cache[i-1], nums[i] + cache[i-2])

        return cache[-1]