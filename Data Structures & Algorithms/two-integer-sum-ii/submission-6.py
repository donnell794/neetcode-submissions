class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for left in range(size):
            right = left + 1
            while right < size and nums[left] + nums[right] <= target:
                if nums[left] + nums[right] == target:
                    return [left+1, right+1]
                right += 1

        
                
