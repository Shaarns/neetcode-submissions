class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 1, 2, 8]
        #[48, 24, 6, 1]
        
        res = []
        last_product = 1
        
        for num in nums:
            res.append(last_product)
            last_product *= num

        last_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = last_product * res[i]
            last_product = last_product * nums[i]
        
        
        return res




