class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False

        target = nums_sum / 2
        target_set = {0}

        for i in range(len(nums)):
            s = target_set.copy()
            for t in s:
                target_set.add(t + nums[i])
            if target in target_set:
                return True

        return False