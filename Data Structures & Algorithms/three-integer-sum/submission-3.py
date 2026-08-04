class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        num_set = set()

        for i, n in enumerate(nums):
            if n > 0:
                break
            left = i+1
            right = size-1
            while left < right:
                three_sum = n + nums[left] + nums[right]
                if three_sum == 0:
                    num_set.add(tuple(sorted([n,nums[left],nums[right]])))
                    left += 1
                    right -= 1

                if three_sum < 0:
                    left += 1
                    continue
                if three_sum > 0:
                    right -= 1
                    continue

        return [] if not num_set else [list(x) for x in num_set]