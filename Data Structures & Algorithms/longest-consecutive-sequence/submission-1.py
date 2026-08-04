class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = []
        nums_set = set(nums)
        for n in nums:
            if n-1 not in nums_set:
                x = n
                seq = 0
                while x in nums_set:
                    seq += 1
                    x += 1
                seqs.append(seq)
            continue

        return max(seqs) if seqs else 0
