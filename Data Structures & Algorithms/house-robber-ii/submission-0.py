class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(start, end):
            prev, curr, temp = 0, 0, 0
            for i in range(start, end):
                temp = max(nums[i] + prev, curr)
                prev = curr
                curr = temp

            return temp

        amount1, amount2 = helper(0, len(nums) - 1), helper(1, len(nums))
        return max(nums[0], amount1, amount2)
