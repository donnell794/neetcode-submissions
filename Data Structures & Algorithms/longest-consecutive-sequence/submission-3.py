class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ret = 0
        for n in nums:
            l = 1
            t = n
            while t+1 in s:
                l += 1
                t += 1
            ret = max(ret, l)

        return ret