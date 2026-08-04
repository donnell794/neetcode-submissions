class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] += 1

        for key,val in count.items():
            freq[val].append(key)

        res = []
        for li in freq[::-1]:
            for l in li:
                res.append(l)
                if len(res) == k:
                    return res

        return res
