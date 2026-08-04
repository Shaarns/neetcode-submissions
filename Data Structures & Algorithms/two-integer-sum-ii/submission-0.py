class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        obj = {}
        findNum = 0

        for i in range(len(numbers)):
            findNum = target - numbers[i]

            if(findNum in obj):
                return[obj[findNum], i+1]

            obj[numbers[i]] = i+1
