class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        nums_set = set(nums)
        for n in nums:
            if n-1 not in nums_set:
                x = n
                seq = 0
                while x in nums_set:
                    seq += 1
                    x += 1
                max_seq = max(max_seq, seq)
            continue

        return max_seq
