class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        heap = []
        i = 0
        while i < len(nums):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k-1:
                while heap[0][1] not in range(i, i-k, -1):
                    heapq.heappop(heap)
                res.append(-heap[0][0])
            i += 1

        return res