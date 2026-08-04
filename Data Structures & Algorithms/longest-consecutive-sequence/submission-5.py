class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        
        for n in nums:
            seq = 1
            temp = n + 1
            while temp in s:
                seq += 1
                temp += 1
            longest = max(longest, seq)

        return longest
