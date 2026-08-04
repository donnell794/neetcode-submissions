class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        while l < r:
            lr_sum = nums[l] + nums[r]
            if lr_sum < target:
                l += 1
            elif lr_sum > target:
                r -= 1
            else:
                return [l+1,r+1]
        return []
