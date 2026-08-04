class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t_sums = {}
        for i,n in enumerate(nums):
            t_sums[target-n] = i

        for j,y in enumerate(nums):
            if t_sums.get(y) and t_sums.get(y) != j:
                return [j, t_sums.get(y)]