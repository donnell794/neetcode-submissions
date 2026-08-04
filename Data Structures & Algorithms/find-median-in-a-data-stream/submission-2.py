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
        # pull from biggest if sizes uneven
        if len(self.small) != len(self.large):
            med = max(self.small, self.large, key=lambda x: len(x))[0]
            return med * -1 if med == self.small[0] else med
        # pull from both if sizes even
        med = []

        if self.small:
            med.append(self.small[0]*-1)
        if self.large:
            med.append(self.large[0])

        return sum(med)/len(med)
        