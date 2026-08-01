class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[2, 3, 4, 5, 6, 7, 8, 9]
        # i,j
        # j,  i,

        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if(j == i): continue
                product = product * nums[j]
            
            res.append(product)
        return res

            


        
        