class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            prod[i] = pre
            pre *= nums[i]

        post = 1
        for j in range(len(nums)-1, -1, -1):
            prod[j] *= post
            post *= nums[j]
        
        return prod