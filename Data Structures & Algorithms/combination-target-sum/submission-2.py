class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []

        def dfs(i, curr, total_sum):
            if total_sum == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total_sum > target:
                return

            curr.append(nums[i])
            dfs(i, curr, nums[i] + total_sum)

            curr.pop()
            dfs(i+1, curr, total_sum)

        dfs(0, curr, 0)
        return res