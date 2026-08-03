class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        lastProd = 1
        for num in nums:
            res.append(lastProd)
            lastProd *= num

        lastProd = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= lastProd
            lastProd = lastProd * nums[i]
        print(res)
        return res

        
        #brute force
        # res = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if(j == i): continue
        #         product = product * nums[j]
            
        #     res.append(product)
        # return res

            


        
        