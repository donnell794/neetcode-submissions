class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        size = len(nums)

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and n == nums[i-1]:
                continue

            left, right = i + 1, size - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                    continue
                if s > 0:
                    right -= 1
                    continue
                ret.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1

        return ret