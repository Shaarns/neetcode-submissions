class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        l = 0
        r = len(nums)-1

        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                nums[r] = "_"
                r -= 1
                k -= 1
            else:
                l += 1

        return k