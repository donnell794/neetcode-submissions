class Solution:
    import heapq
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = -math.sqrt((0-point[0])**2 + (0-point[1])**2)
            heapq.heappush(heap, [distance, point])
            if len(heap) > k:
                heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for x in range(k)]