class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {n:i for i,n in enumerate(nums)}
        for i in range(len(nums)-1, -1, -1,):
            n = nums[i]
            if target-n in d and i != d[target-n]:
                return [d[target-n]+1, i+1]
