class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l

        pre = 1
        for i,n in enumerate(nums):
            res[i] *= pre
            pre *= n

        post = 1
        for i in range(l-1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res