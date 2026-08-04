class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #[9,1,4,7,-1,0,3,5,8,-1,6]
        obj = {}
        for num in nums:
            obj[num] = 1

        maxConsecCount = 0

        for num in nums:
            count = 0
            if num - 1 in obj:
                continue
            else:
                nextNum = num
                while nextNum in obj:
                    count += 1
                    nextNum += 1
                if(maxConsecCount < count):
                    maxConsecCount = count
                        




            
        return maxConsecCount
         
    