class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #[6, 7, 8, 1, 2, 3, 4] t = 0
        #[3,5,6,0,1,2]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2

            if target == nums[m]:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1                
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1



        return -1
        
            
    