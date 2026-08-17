class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniqueNum = set()

        for num in nums:
            if num in uniqueNum:
                uniqueNum.remove(num)
            else:
                uniqueNum.add(num)
                
        return uniqueNum.pop()
            