class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            diff = target - n
            d[diff] = i

        for j, m in enumerate(nums):
            if m in d and j != d[m]:
                return [j, d[m]]