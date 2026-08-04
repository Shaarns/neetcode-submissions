class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #[9,1,4,7,-1,0,3,5,8,-1,6]
        numSet = set(nums)

        maxConsecCount = 0

        for num in numSet:
            count = 0
            if num - 1 in numSet:
                continue
            else:
                nextNum = num
                while nextNum in numSet:
                    count += 1
                    nextNum += 1
                maxConsecCount = max(maxConsecCount, count)
                        
        return maxConsecCount
         
    