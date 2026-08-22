class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        #[4, 5, 6]
        #k=2, k=1, k=0

        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0] if nums else 0