class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        for point in points:
            x = point[0]
            y = point[1]

            distance = (x ** 2) + (y ** 2)

            heapq.heappush(min_heap, (distance, point))

        res = []

        while k:
            k -= 1
            dis = heapq.heappop(min_heap)
            res.append(dis[1])

        return res

