class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        if len(stones) == 1: return stones[0]
        sorted_stones = [x*-1 for x in stones]
        heapq.heapify(sorted_stones)
        print(sorted_stones)

        while sorted_stones and len(sorted_stones) > 1:
            weight1 = -(heapq.heappop(sorted_stones))
            weight2 = -(heapq.heappop(sorted_stones))
            new_weight = weight1 - weight2

            if new_weight:
                heapq.heappush(sorted_stones, -(new_weight))

        return (-sorted_stones[0] if sorted_stones else 0)


