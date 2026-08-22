class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        print(stones)

        i = len(stones)-1
        j = len(stones)-2

        while j >= 0:
            stones[j] = stones[i] - stones[j]
            i -= 1
            j -= 1
            stones.sort()
        return stones[0]