class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        list_items = set()

        for num in nums:
            if num in list_items:
                return num
            list_items.add(num)

        return