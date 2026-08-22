class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        print(points)
        min_heap = []
        heapq.heapify(min_heap)
        print(min_heap)

        for point in points:
            x = point[0]
            y = point[1]

            distance = (x ** 2) + (y ** 2)

            heapq.heappush(min_heap, (distance, point))

        print(min_heap[0])
        res = []

        while k:
            k -= 1
            dis = heapq.heappop(min_heap)
            print("dis", dis)
            res.append(dis[1])

        return res

