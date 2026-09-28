class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return

            if curr_sum > target or i >= len(nums):
                return

            if curr_sum <= target:
                curr.append(nums[i])
                backtrack(i, curr_sum + nums[i])

            curr.pop()
            backtrack(i+1, curr_sum)

        backtrack(0, 0)
        return res
            
