class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = [-1*num for num in nums]
        heapq.heapify(sorted_nums)

        while k > 1:
            heapq.heappop(sorted_nums)
            k -= 1

        return -(heapq.heappop(sorted_nums))