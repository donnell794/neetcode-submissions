import heapq
class MedianFinder:

    def __init__(self):
        self.first = []
        self.second = []

    def addNum(self, num: int) -> None:
        if self.first and num > -self.first[0]:
            heapq.heappush(self.second, num)
        else:
            heapq.heappush(self.first, -num)
        
        self.balance()
        
    def balance(self):
        if len(self.first) - len(self.second) > 1:
            heapq.heappush(
                self.second,
                -heapq.heappop(self.first)
            )

        elif len(self.second) - len(self.first) > 1:
            heapq.heappush(
                self.first,
                -heapq.heappop(self.second)
            )

    def findMedian(self) -> float:
        if len(self.first) > len(self.second):
            return -self.first[0]
        elif len(self.second) > len(self.first):
            return self.second[0]

        return (-self.first[0] + self.second[0]) / 2
        