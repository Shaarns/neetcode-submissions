class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}

        for i, num in enumerate(nums):
            x = target - num

            if x in obj:
                return [obj[x], i]

            obj[num] = i