class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        pre = 1
        for i,n in enumerate(nums):
            prod[i] *= pre
            pre *= n

        post = 1
        for i in range(len(nums)-1, -1, -1):
            prod[i] *= post
            post *= nums[i]

        return prod