class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, cnt in count.items():
            if cnt > (len(nums)/2):
                return num
