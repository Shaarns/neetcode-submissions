class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

        heapq.heapify(self.left_max_heap)
        heapq.heapify(self.right_min_heap)

    def addNum(self, num: int) -> None:
        if self.right_min_heap and self.right_min_heap[0] < num:
            heapq.heappush(self.right_min_heap, num)
        else:
            heapq.heappush(self.left_max_heap, -num)

        while (len(self.left_max_heap) - len(self.right_min_heap)) > 1:
            left_max_num = -(heapq.heappop(self.left_max_heap))
            heapq.heappush(self.right_min_heap, left_max_num)

        while (len(self.right_min_heap) - len(self.left_max_heap)) > 1:
            right_min_num = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -right_min_num)
        

    def findMedian(self) -> float:
        median = None
        if len(self.left_max_heap) == len(self.right_min_heap):
            median = (-(self.left_max_heap[0]) + self.right_min_heap[0]) / 2

        elif len(self.left_max_heap) > len(self.right_min_heap):
            median = -self.left_max_heap[0]

        elif len(self.left_max_heap) < len(self.right_min_heap):
            median = self.right_min_heap[0]
        
        return median