class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        suffix = [0] * len(nums)
        last_product = 1
        for i in range(1, len(nums)):
            last_product = last_product * nums[i-1]
            prefix.append(last_product)

        last_product = 1
        suffix[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            last_product = last_product * nums[i+1]
            suffix[i] = last_product
        
        product = []
        for i in range(len(nums)):
            product.append( prefix[i] * suffix[i])
        return product




