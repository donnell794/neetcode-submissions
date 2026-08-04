class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            s1, s2 = [-heapq.heappop(heap) for _ in range(2)]
            if s1 == s2:
                continue
            heapq.heappush(heap, -(s1 - s2))

        return -heap[0] if heap else 0