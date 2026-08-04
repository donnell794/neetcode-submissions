class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,n in enumerate(nums):
            s[target-n] = i

        for i,n in enumerate(nums):
            if n in s and i != s[n]:
                return [i, s[n]]
