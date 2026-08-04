class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = float('-inf')

        for n in nums:
            curr_sum = max(curr_sum, 0) + n
            max_sum = max(max_sum, curr_sum)
        
        return max_sum