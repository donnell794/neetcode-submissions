class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in nums:
            if n-1 in s:
                continue
        
            l = 0
            while n+l in s:
                l += 1
            longest = max(longest, l)

        return longest