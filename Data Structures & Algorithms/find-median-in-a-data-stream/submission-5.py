import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num >= self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        self.balance()


    def balance(self):
        size_small = len(self.small)
        size_large = len(self.large)

        if size_small > size_large+1:
            heapq.heappush(
                self.large,
                -heapq.heappop(self.small)
            )
        elif size_large > size_small+1:
            heapq.heappush(
                self.small,
                -heapq.heappop(self.large)
            )


    def findMedian(self) -> float:
        size_small = len(self.small)
        size_large = len(self.large)

        if size_small > size_large:
            return -self.small[0]

        if size_large > size_small:
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2
        