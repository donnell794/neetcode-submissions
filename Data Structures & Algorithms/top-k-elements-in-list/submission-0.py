import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        top_k = heapq.nlargest(n=k, iterable=freq.items(), key=lambda x: x[1])

        return [x[0] for x in top_k]