class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prod = [1] * l

        pre = 1
        for i in range(l):
            prod[i] *= pre
            pre *= nums[i]

        post = 1
        for i in range(l-1, -1, -1):
            prod[i] *= post
            post *= nums[i]

        return prod
