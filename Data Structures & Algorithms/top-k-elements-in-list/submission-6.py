class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        rfreq = {}
        for key, val in freq.items():
            if val not in rfreq:
                rfreq[val] = []
            rfreq[val].append(key)

        res = []
        
        for i in range(len(nums), 0, -1):
            if i in rfreq:
                res.extend(rfreq[i])

        return res[:k]

