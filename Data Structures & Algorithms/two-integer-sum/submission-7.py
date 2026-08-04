class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i,n in enumerate(nums):
            d[target - n] = i

        for i,n in enumerate(nums):
            if n in d and i != d[n]:
                return [i, d[n]]