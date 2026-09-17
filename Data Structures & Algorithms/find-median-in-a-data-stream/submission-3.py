class MedianFinder:

    def __init__(self):
        # min heap
        self.small = [] # max heap
        self.large = [] # min heap
        # heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, (-1 * num))

        # all ele in small has to be  < those in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, (-1 * heapq.heappop(self.small)))

        # if the uneven size
        if len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, (-1 * heapq.heappop(self.small)))
        if len(self.large) - len(self.small) > 1:
            heapq.heappush(self.small, (-1 * heapq.heappop(self.large)))
        
    def findMedian(self) -> float:
        
        if len(self.small) > len(self.large):
            return (-1 * self.small[0])
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + self.large[0]) / 2.0

    
        
        