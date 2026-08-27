class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, curr = [], []

        def dfs(i, curr, total_sum):
            if total_sum == target:
                res.append(curr.copy())
                return

            if total_sum > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            dfs(i+1, curr, total_sum + candidates[i])
            curr.pop()

            while(i+1 < len(candidates) and candidates[i] == candidates[i+1]):
                i += 1

            dfs(i+1, curr, total_sum)

        dfs(0, curr, 0)
        return res
            
            