class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]
        size = len(nums)
        nprod = 1

        for i in range(1, size):
            product.append(product[i-1]*nums[i-1])

        for j in range(size-1, -1, -1):
            product[j] *= nprod
            nprod *= nums[j]
        
        return product
