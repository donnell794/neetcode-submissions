class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        front, back = 0, size-1

        while 1:
            int_sum = sum([nums[front], nums[back]])

            if int_sum == target:
                return [front+1, back+1]

            if int_sum < target:
                front += 1

            if int_sum > target:
                back -= 1