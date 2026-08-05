class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        rfreq = {}
        for key,v in freq.items():
            if v not in rfreq:
                rfreq[v] = []
            rfreq[v].append(key)
        
        kfreq = []
        i = len(nums)
        while len(kfreq) < k and i >= 0:
            if i in rfreq:
                kfreq.extend(rfreq[i])
            i -= 1
            
        return kfreq