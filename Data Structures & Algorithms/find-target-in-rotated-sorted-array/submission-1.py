class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l1 = 0
        r1 = r2 = len(nums)-1

        if nums[0] == target: return 0

        while nums[l1] > nums[r1]:
            r1 -= 1

        l2 = r1+1
        print(l2)

        def binary_search(l, r):
            while l <= r:
                m = (l+r)//2

                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return False
            
        bn1 = binary_search(l1, r1)
        bn2 = binary_search(l2, r2)
        return bn1 or bn2 or -1

        
        