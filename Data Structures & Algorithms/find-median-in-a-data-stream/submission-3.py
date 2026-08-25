class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        l = 0
        r = len(self.arr) - 1
        mid = (l+r)//2
        median = None

        if len(self.arr) % 2 == 0:
            median = (self.arr[mid] + self.arr[mid+1]) / 2
        else:
            median = self.arr[mid]
        
        return median