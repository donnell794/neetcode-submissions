class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import defaultdict

        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        heap = []
        for n in d:
            heap.append((d[n], n))

        # heapq.heapify(heap)

        return [x[1] for x in heapq.nlargest(k, heap)]