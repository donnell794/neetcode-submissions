class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 0
        # 2 , -2
        # 4 0 , 0 -4
        # 6 2 2 -2 , 2 -2 -2 -6
        sums = [0]
        for n in nums:
            new_sums = []
            for s in sums:
                new_sums.append(s+n)
                new_sums.append(s-n)
            sums = new_sums
        return sums.count(target)