class Solution:
    import heapq
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        heap = []
        for i,n in enumerate(nums):
            heapq.heappush(heap, (-n, i))
            if i >= k-1:
                while heap[0][1] < i-k+1:
                    heapq.heappop(heap)
                res.append(-heap[0][0])

        return res