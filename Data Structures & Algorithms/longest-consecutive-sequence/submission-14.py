class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0

        count = 0
        for i in range(len(nums)):

            if i == 0:
                count += 1
                longest = max(longest, count)
                continue

            elif nums[i] == nums[i-1]: continue
            elif nums[i] - 1 == nums[i - 1]:
                count += 1

                longest = max(longest, count)

            else:
                count = 1
        print(nums)
        return longest