import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        # add to max
        if self.large and num >= self.large[0]:
            heapq.heappush(self.large, num)
        else:
        # or add to min
            heapq.heappush(self.small, num * -1)
        # rebalance if necessary
        self.balance()

    def balance(self):
        while (len(self.small) - len(self.large)) > 1:
            heapq.heappush(self.large,(heapq.heappop(self.small) * -1))
            

        while (len(self.large) - len(self.small)) > 1:
            heapq.heappush(self.small,(heapq.heappop(self.large) * -1))

    def findMedian(self) -> float:
        size_small = len(self.small)
        size_large = len(self.large)

        if size_small > size_large:
            return self.small[0] * -1
        elif size_large > size_small:
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2
        