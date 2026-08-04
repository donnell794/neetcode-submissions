import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        for key,val in freq.items():
            heapq.heappush(heap, (-val, key))

        return [heapq.heappop(heap)[1] for _ in range(k)]

        
