class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        min_elem = float('inf')

        while l <= r:
            m = (l+r)//2

            min_elem = min(min_elem, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1 



        return min_elem

        