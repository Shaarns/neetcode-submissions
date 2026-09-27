class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []

        def subset(i):
            if i >= len(nums):
                res.append(curr.copy())
                return

            #include nums[i]
            curr.append(nums[i])
            subset(i+1)
            curr.pop()

            #don't include nums[i]
            subset(i+1)

        subset(0)
        return res
            


            
