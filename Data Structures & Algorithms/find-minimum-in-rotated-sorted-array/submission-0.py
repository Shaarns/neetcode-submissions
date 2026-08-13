class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r2 = r1 = len(nums) - 1
        min_elem = float('inf')

        while nums[l] > nums[r1]:
            r1 -= 1
        
        l2 = r1 + 1
        while l <= r1:
            m = (l+r1)//2

            min_elem = min(min_elem, nums[m])
            if min_elem >= nums[m]:
                r1 = m-1

        while l2 <= r2:
            m = (l2+r2)//2

            min_elem = min(min_elem, nums[m])
            if min_elem >= nums[m]:
                r2 = m-1

        return min_elem

        