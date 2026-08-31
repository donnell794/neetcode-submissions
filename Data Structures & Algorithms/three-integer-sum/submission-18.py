class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, ln = [], len(nums)-1
        for i,n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue

            l, r = i+1, ln
            while l < r:
                t = n + nums[l] + nums[r]
                if t < 0:
                    l += 1
                elif t > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 
        return res

